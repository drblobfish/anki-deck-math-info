# anki-deck-math-info
deck anki pour réviser les cours de licence math-info


# Installation

Cloner le répository quelque part.
- Ouvrez un terminal dans le dossier approprié
- Taper `git clone git@github.com:drblobfish/anki-deck-math-info.git`

Lancer Anki. Cliquer Fichier/Importer. Sélectionner le fichier `Analyse.txt`.
CLiquer sur Importer dans le fenêtre affichée. Renommer le nouveau deck 
`Default` avec un nom approprié.

# Modifier et partager le deck

## Si vous êtes collaborateur du repo sur github

Modifier le deck avec l'interface de anki.

Cliquer sur Fichier/Exporter.
Rentrer les paramètres suivants :
- Format d'export : Note en texte (.txt)
- Inclure : Analyse 4
- Inclure les référence HTML et médiatique
- Inclure les tags
- Inclure le nom du paquet

Cliquer exporter et écraser le fichier `Analyse.txt` dans le dossier git

Ouvrez un terminal dans votre dossier git
entrer `git add -A;git commit -m"description des modifications";git push`

## Si vous n'êtes pas collaborateur du repo

Vous pouvez me demander à être ajouté.
Sinon, il faudra faire un fork du repository, modifier sur votre fork 
puis faire un pull request. Pour cela, se référer à la documentation de
git et de github.

# Mise à jour du deck

Naviger dans votre dossier git et taper `git pull`
Lancer Anki, puis Fichier/Importer et sélectionner Analyse 4


# Style des cartes, conseils pour l'édition de cartes

- Faire des cartes courtes
- Utiliser un champ MathJax en ligne pour taper les éléments mathématiques
  LaTeX
- Ne pas oublier toutes les hypothèse des théorèmes
- Ne pas utiliser la numérotation du cours (pas de question comme "énoncer
  le théorème 3.8")
- ...
(à continuer)

# Autre contribution possible

La base de donnée anki peut être modifiée en python. Pour cela, il faut utiliser
le module anki associé (`pip install anki`). Voir [la documentation](https://addon-docs.ankiweb.net/command-line-use.html).
Un bon projet serait de coder un petit script python pour mettre à jour le 
deck avec une seule ligne de commande.
Le script s'occuperait d'effectuer les commandes git par lui même et de mettre
à jour le base de donnée d'anki.
Mes premiers tests pour la création du script peuvent être trouvée dans le 
fichier `update`.
Si quelqu'un a la motivation, la documentation de anki n'est pas trop mauvaise.








