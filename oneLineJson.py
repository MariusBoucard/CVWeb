multiline_string = """

Mon expérience chez **Slate Digital** a débuté par un **stage de 6 mois**, durant lequel j’ai eu l’opportunité de découvrir leur stack technique en menant le **portage de leurs plugins audio sur IOS**.
Cela a nécessité la **création du support pour le format AUv3**, un format spécifique aux plugins audio sur **IOS**, ainsi que **l’adaptation du framework interne** à cette nouvelle plateforme. J’ai travaillé sur l’**implémentation des APIs adaptées** et sur **l’interprétation des messages** émis par l’iPad, en m’assurant du bon fonctionnement de l’interface et des performances des traitements audio.
Ce travail a permis à plusieurs plugins développés par Slate Digital de fonctionner efficacement sur iPad, avec des résultats convaincants en termes de performance et d’expérience utilisateur.
Ce stage m’a permis de **comprendre en profondeur la structure d’un plugin audio**, ainsi que les spécificités d’un développement sur une plateforme mobile.
L’expérience acquise a ensuite été directement mise à profit dans le cadre de mon **CDI** au sein de la même entreprise, où je continue à contribuer au développement de leurs logiciels.

"""

multiline_string2 = """
Stage de 2 mois réalisé durant l’été 2023 chez **Coexya**, au sein du pôle éditique.
L’objectif principal était de faire évoluer une application interne nommée *Compote*, développée avec **VueJS** et déployée via **Electron**.

Mon travail a consisté à concevoir et intégrer de nouvelles fonctionnalités, notamment un système de **lancement en batch de scripts** à destination d’un moteur utilisé en production.
L’outil, destiné à un public interne non technique, nécessitait une **interface claire, simple et accessible**, tout en respectant les contraintes fonctionnelles du pôle.

Ce stage m’a permis de :

* Appliquer VueJS dans un **contexte professionnel structuré** ;
* Développer des **features concrètes répondant à des besoins métiers réels** ;
* Contribuer à un outil utilisé en production, dans un environnement d’entreprise ;
* Approfondir l’usage de **Electron** pour le déploiement d’applications desktop internes.

"""
multiline_string3 = """

Semestre universitaire réalisé en début d’année 2023 à **Newcastle University**, dans le cadre d’un programme Erasmus+.
Cette expérience m’a permis de renforcer significativement mes **compétences en anglais**, tant à l’écrit qu’à l’oral, grâce à un environnement académique entièrement anglophone.

Le cursus, axé sur la **lecture et l’analyse de publications scientifiques**, m’a également initié à la **recherche académique** à travers des travaux approfondis sur des articles spécialisés.

Le rythme plus flexible de la formation m’a offert l’opportunité de consacrer du temps à des **projets personnels** variés, en développement web et audio, me permettant d’expérimenter de nouveaux outils et d’approfondir mes centres d’intérêt techniques.

"""

multiline_string4 = """
Cursus suivi en formation initiale à l’INSA de Rennes, au sein du département Informatique, après deux années de prépa intégrée. Ce parcours académique exigeant et complet m’a permis d’acquérir une vision large et structurée des fondamentaux de l’informatique, en explorant aussi bien les aspects théoriques (algorithmique, réseaux, architecture…) que pratiques (développement logiciel, bases de données, systèmes distribués…).

Au cours de cette formation, j’ai choisi de me spécialiser en Data Science, ce qui m’a permis d’approfondir mes compétences en analyse de données, apprentissage automatique, statistiques et visualisation, tout en consolidant ma compréhension des enjeux liés à l’exploitation intelligente des données.

La diversité et la richesse des enseignements m’ont permis de développer une base solide de connaissances générales, tout en mettant en œuvre ces acquis à travers des projets concrets.

Les concepts assimilés durant cette période jouent aujourd’hui un rôle clé dans ma capacité à comprendre les contraintes techniques d’un projet, à faire des choix pertinents en matière d’architecture ou de développement, et à anticiper les implications de ces décisions dans un cadre professionnel.
"""


multiline_string5 = """


Développement et maintien d’un site web *sur mesure* pour **L’Agrafe**, une association étudiante de l’Université **Rennes 2**.
Ce projet, mené de manière **autonome** en parallèle de mes études, a permis de concevoir une **application web** répondant à des besoins *spécifiques* exprimés par le comité de rédaction. 
Grace à des *échanges réguliers* nous avons **analysé les usages souhaités**, défini les **priorités fonctionnelles**, puis développé une **interface simple et intuitive** destinée à un public *non technique*. Aucun membre de l'association n'étant développeur.

Le site repose sur une **architecture Node** :

* **Frontend** développé en *VueJS*
* **Backend** géré avec *ExpressJS*

Ce projet m’a permis de renforcer mes compétences en **conception orientée utilisateur**, en **gestion de projet web**, et en **autonomie technique**.
J’en assure toujours la **maintenance** et les **évolutions fonctionnelles**.

*Cf : Plus d'informations dans la rubrique projets.*

"""
multiline_string6 = """
**Développement** d’un site personnel visant à **centraliser** et **archiver** des **compositions musicales** réalisées en collaboration. Le site repose sur une architecture **VueJS** (frontend) et **ExpressJS** (backend), avec une base de données **MySQL** pour la gestion des contenus. Cette structure, héritée du projet **_L’Agrafe_**, assure une **cohérence technique** et une bonne **maintenabilité**.

L’interface permet de :
- **Parcourir** les morceaux,
- **Consulter** leurs détails,
- Accéder à l’ensemble des compositions via une **bibliothèque centralisée**.

### Ce projet a permis de :
- **Réutiliser** une architecture fullstack éprouvée (**VueJS**, **ExpressJS**, **MySQL**) ;
- **Concevoir** un système d’**archivage structuré** pour contenus musicaux ;
- **Approfondir** l’utilisation de bases de données relationnelles dans un contexte applicatif simple.
"""

# Convert to a single line with \n
single_line_string = multiline_string6.strip().replace("\n", "\\n")

print(single_line_string)