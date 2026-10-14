# ajej.ma

Site statique bilingue de l'Association Jisr pour l'Enfance et la Jeunesse.

## Pages

Les versions arabe et française comprennent l'accueil, la présentation de
l'association, les domaines d'action, les activités, la participation, le
contact et la page de l'Université des jeunes (octobre 2026).
L'annonce d'adhésion de la section de Midelt (17 octobre 2026) a une page
distincte, avec son affiche et ses informations pratiques. Elle ne doit pas
être présentée comme une annonce nationale.
Une page « Impact et transparence » distingue les annonces des bilans
documentés, en arabe et en français.
La page dédiée à l'Université des jeunes comprend des données structurées
Event limitées aux faits publiés (dates sans horaires, lieu et affiche).
Après le 24 octobre 2026, le script masque les promotions de participation
et affiche une note d'archive sur l'annonce, sans supposer que l'activité
a eu lieu. Le compte rendu devra être ajouté après validation des faits.
L'annonce de Midelt est mise en avant jusqu'au 17 octobre ; dès le 18,
elle reste consultable dans les activités comme annonce passée. La barre
supérieure revient alors à l'Université des jeunes jusqu'au 24 octobre.

## Mise à jour

Modifier `scripts/build_site.py`, puis lancer `python scripts/build_site.py`.
Le script régénère les deux langues, la page racine et le sitemap. Les styles
et les interactions du menu se trouvent dans `assets/site-2026-compact.css`,
`assets/site-2026-impact.css` et `assets/site-2026.js`. Publier les fichiers
statiques à la racine du dépôt.

Les numéros publiés sont ceux de l'annonce de l'Université des jeunes : ils
ne sont pas présentés comme des coordonnées générales de l'association.

