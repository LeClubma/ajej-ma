const toggle = document.querySelector('.menu-toggle');
const navigation = document.getElementById('site-nav');
if (toggle && navigation) {
  const setOpen = open => {
    navigation.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? toggle.dataset.close : toggle.dataset.open);
  };
  toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setOpen(false)));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });
  document.addEventListener('click', event => {
    if (!navigation.contains(event.target) && !toggle.contains(event.target)) setOpen(false);
  });
}
const year = document.getElementById('year');
if (year) year.textContent = String(new Date().getFullYear());

// Keep a dated announcement available as an archive without promoting a
// participation opportunity after its published dates have passed.
const moroccoDateParts = new Intl.DateTimeFormat('en-GB', {
  timeZone: 'Africa/Casablanca', year: 'numeric', month: '2-digit', day: '2-digit'
}).formatToParts(new Date());
const moroccoDate = Object.fromEntries(moroccoDateParts.map(part => [part.type, part.value]));
const todayInMorocco = [moroccoDate.year, moroccoDate.month, moroccoDate.day].join('-');
if (todayInMorocco > '2026-10-24') {
  document.documentElement.classList.add('event-past');
  document.querySelectorAll('[data-event-promo]').forEach(element => { element.hidden = true; });
  const archiveNote = document.querySelector('[data-event-archive-note]');
  if (archiveNote) archiveNote.hidden = false;
  const listingTitle = document.querySelector('[data-event-list-title]');
  if (listingTitle) listingTitle.textContent =
    document.documentElement.lang === 'ar' ? 'إعلان سابق' : 'Annonce passée';
}
