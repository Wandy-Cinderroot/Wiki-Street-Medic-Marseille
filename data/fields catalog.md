# Général

| categories             | id                     | type               | default | description | requis |
| ---------------------- | ---------------------- | ------------------ | ------- | ----------- | ------ |
| #identification        | #nom                   | Texte (une ligne)  |         |             | oui    |
| #identification        | #slug                  | Texte (une ligne)  |         |             | oui    |
| #identification        | #autres-noms           | Texte long         |         |             | non    |
| #identification        | #resume                | Texte long         |         |             | oui    |
| #identification        | #vignette-image        | Fichier            |         |             | non    |
| #identification        | #vignette-infos        | Texte long         |         |             | non    |
| #sources-et-validation | #sources               | Sélection multiple |         |             |        |
| #sources-et-validation | #derniere-verification | Date               |         |             |        |
| #sources-et-validation | #statut                | Liste déroulante   |         |             |        |
| #sources-et-validation | #contributeur-ice      | Sélection multiple |         |             |        |

## Unités

| categories            | id                       | type               | default                                             | description | requis |
| --------------------- | ------------------------ | ------------------ | --------------------------------------------------- | ----------- | ------ |
| details-technique     | resume                   | Texte long         |                                                     |             |        |
| details-technique     | type-d-unite             | Sélection multiple | intervention , interpellation , maintien de l'ordre |             |        |
| details-technique     | autorite-de-rattachement | Sélection multiple | police , gendarmerie, DGSI                          |             |        |
| details-technique     | organisation             | Texte long         |                                                     |             |        |
| details-technique     | fonctionnement           | Texte long         |                                                     |             |        |
| moyens-et-equipements | armes                    | Sélection multiple |                                                     |             |        |
| moyens-et-equipements | vehicules                | Sélection multiple |                                                     |             |        |

## Armes de contact

| categories           | id                  | type                       | default | description                                                                    | requis |
| -------------------- | ------------------- | -------------------------- | ------- | ------------------------------------------------------------------------------ | ------ |
| utilisation          | cadre-d-utilisation | Sélection multiple         |         | cadre legal d'utilisation de l'arme                                            |        |
| utilisation          | unites-utilisatrice | Sélection multiple         |         | unités pouvant utiliser ces armes                                              |        |
| utilisation          | observations        | Texte long                 |         | utilisation documenté sur le terrain                                           |        |
| risques-et-blessures | types-de-blessures  | Sélection multiple         |         | types de blessures possible à cause de l'arme                                  |        |
| risques-et-blessures | zones-corporelles   | Sélection multiple         |         | type de zones corporelle touché par l'arme                                     |        |
| risques-et-blessures | precautions         | Texte long                 |         | Précautions pour les street-medics à avoir pour prévenir ce genre de blessures |        |
| risques-et-blessures | images de blessures | Fichiers                   |         | image de blessures dû à l'arme                                                 |        |
| details-technique    | description         | Texte long                 |         | description visuel de l'arme                                                   |        |
| details-technique    | distance            | Nombre                     |         | distance en metre                                                              |        |
| details-technique    | fonctionnement      | Texte long                 |         | explication du fonctionnement de l'arme                                        |        |
| details-technique    | materiaux           | Sélection multiple         |         | materiaux composant l'arme                                                     |        |
| details-technique    | fabricant           | Sélection multiple         |         | fabricant construisant ce type d'arme                                          |        |
| details-technique    | modeles             | Fichiers avec descriptions |         | differents modeles de l'arme avec images correspondant                         |        |
## Munitions

| categories           | id                  | type                       | default | description                                                                    | requis |
| -------------------- | ------------------- | -------------------------- | ------- | ------------------------------------------------------------------------------ | ------ |
| utilisation          | cadre-d-utilisation | Sélection multiple         |         | cadre legal d'utilisation de l'arme                                            |        |
| utilisation          | unites-utilisatrice | Sélection multiple         |         | unités pouvant utiliser ces armes                                              |        |
| utilisation          | observations        | Texte long                 |         | utilisation documenté sur le terrain                                           |        |
| risques-et-blessures | types-de-blessures  | Sélection multiple         |         | types de blessures possible à cause de l'arme                                  |        |
| risques-et-blessures | zones-corporelles   | Sélection multiple         |         | type de zones corporelle touché par l'arme                                     |        |
| risques-et-blessures | precautions         | Texte long                 |         | Précautions pour les street-medics à avoir pour prévenir ce genre de blessures |        |
| risques-et-blessures | images de blessures | Fichiers                   |         | image de blessures dû à l'arme                                                 |        |
| details-technique    | description         | Texte long                 |         | description visuel de l'arme                                                   |        |
| details-technique    | fonctionnement      | Texte long                 |         | explication du fonctionnement de l'arme                                        |        |
| details-technique    | calibre             | Sélection multiple         |         | calibre de la munition                                                         |        |
| details-technique    | lanceurs            | Sélection multiple         |         | lanceurs compatible avec la munition                                           |        |
| details-technique    | materiaux           | Sélection multiple         |         | materiaux composant l'arme                                                     |        |
| details-technique    | fabricant           | Sélection multiple         |         | fabricant construisant ce type d'arme                                          |        |
| details-technique    | modeles             | Fichiers avec descriptions |         | differents modeles de l'arme avec images correspondant                         |        |
## Lanceurs

| categories           | id                  | type                       | default | description                                                                    | requis |
| -------------------- | ------------------- | -------------------------- | ------- | ------------------------------------------------------------------------------ | ------ |
| utilisation          | cadre-d-utilisation | Sélection multiple         |         | cadre legal d'utilisation de l'arme                                            |        |
| utilisation          | unites-utilisatrice | Sélection multiple         |         | unités pouvant utiliser ces armes                                              |        |
| utilisation          | observations        | Texte long                 |         | utilisation documenté sur le terrain                                           |        |
| risques-et-blessures | types-de-blessures  | Sélection multiple         |         | types de blessures possible à cause de l'arme                                  |        |
| risques-et-blessures | zones-corporelles   | Sélection multiple         |         | type de zones corporelle touché par l'arme                                     |        |
| risques-et-blessures | precautions         | Texte long                 |         | Précautions pour les street-medics à avoir pour prévenir ce genre de blessures |        |
| risques-et-blessures | images de blessures | Fichiers                   |         | image de blessures dû à l'arme                                                 |        |
| details-technique    | description         | Texte long                 |         | description visuel de l'arme                                                   |        |
| details-technique    | fonctionnement      | Texte long                 |         | explication du fonctionnement de l'arme                                        |        |
| details-technique    | calibre             | Sélection multiple         |         | calibre de la munition                                                         |        |
| details-technique    | munitions           | Sélection multiple         |         | munitions compatible avec le lanceur                                           |        |
| details-technique    | fabricant           | Sélection multiple         |         | fabricant construisant ce type d'arme                                          |        |
| details-technique    | modeles             | Fichiers avec descriptions |         | differents modeles de l'arme avec images correspondant                         |        |
## Véhicules

| categories        | id                  | type               | default | description                             | requis |
| ----------------- | ------------------- | ------------------ | ------- | --------------------------------------- | ------ |
| utilisation       | cadre-d-utilisation | Sélection multiple |         | cadre legal d'utilisation de l'arme     |        |
| utilisation       | unites-utilisatrice | Sélection multiple |         | unités pouvant utiliser ces armes       |        |
| utilisation       | observations        | Texte long         |         | utilisation documenté sur le terrain    |        |
| details-technique | description         | Texte long         |         | description visuel de l'arme            |        |
| details-technique | fonctionnement      | Texte long         |         | explication du fonctionnement de l'arme |        |
| details-technique | equipements         | Sélection multiple |         | équipement du vehicule                  |        |
| details-technique | fabricant           | Sélection multiple |         | fabricant construisant ce type d'arme   |        |
| details-technique | type                | Sélection multiple |         | type de vehicule                        |        |
