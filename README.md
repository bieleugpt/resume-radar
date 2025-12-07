1. Répartition pour les livrables académiques (Proposal, State of the Art, Final Report)
Personne A — Méthodologie technique / Architecture du modèle
Responsable de :
•	ligne directrice technique du projet,
•	description des modèles (U-Net, SRN, GAN léger),
•	section "Methodology" du rapport,
•	figures expliquant l’architecture,
•	description du pipeline de restauration.
Personne B — OCR, Évaluation, Analyse
Responsable de :
•	pipeline OCR,
•	choix et justification des métriques (PSNR, SSIM, CER),
•	section "Experiments" et "Results" du rapport,
•	tableaux, graphiques, analyses quantitatives.
Tâches communes (réparties mais simultanées)
•	Proposal (chacun rédige les parties liées à sa pipeline).
•	State of the Art (A écrit sur les méthodes de défloutage, B sur OCR + metrics).
•	Introduction / Conclusion (rédigées ensemble pour cohérence).
________________________________________
2. Répartition technique — Deux pipelines indépendants
Pipeline 1 : Restauration d’image — Personne A
Travail totalement autonome, directement aligné avec “Image enhancement / restoration” du cours.
Tâches indépendantes
1.	Télécharger datasets (RealBlur, ICDAR, SynthText).
2.	Générer flous artificiels (motion blur, gaussian, compression).
3.	Implémenter :
o	U-Net,
o	Scale-Recurrent Network,
o	GAN léger.
4.	Entraîner, comparer, optimiser les modèles.
5.	Déposer des images restaurées dans un dossier partagé (pour B).
A peut tout faire sans attendre B.
________________________________________
Pipeline 2 : OCR et Évaluation — Personne B
Tâches indépendantes
1.	Installer / configurer OCR (Tesseract ou PaddleOCR).
2.	Tester OCR sur images floues pour baseline.
3.	Coder les métriques :
o	PSNR,
o	SSIM,
o	CER/WER.
4.	Construire les scripts :
o	tableaux de résultats,
o	courbes d’erreurs,
o	comparaisons visuelles.
B n’a pas besoin du travail de A pour avancer au début.
________________________________________
3. Point de jonction (court et non bloquant)
Quand A produit les premières images restaurées,
B les insère simplement dans son pipeline OCR déjà prêt.
La seule dépendance du projet est donc :
➡️ 1 dossier : “restored_images/”
Tout le projet est pensé pour éviter une dépendance bloquante.
________________________________________
4. Phase finale : Fusion pour le rapport et la présentation
À la fin :
Personne A fournit
•	images restaurées,
•	notes de comparaison entre modèles,
•	figures techniques (architecture, training curves).
Personne B fournit
•	analyse OCR (avant / après),
•	PSNR / SSIM / CER complets,
•	visualisations et tableaux,
•	interprétation des résultats.
Les deux pipelines se rejoignent naturellement dans le rapport final.
________________________________________
5. Pourquoi cette organisation est parfaite pour la note finale
•	Elle permet de couvrir toutes les attentes de Ruiwen :
o	projet original,
o	vision multimodale (image restoration + OCR),
o	comparaison de modèles,
o	analyse quantitative solide,
o	rapport structuré comme une publication.
•	Elle garantit que chaque membre contribue réellement (critère de participation).
•	Elle évite qu’un retard technique d’un côté bloque l’autre.
•	Elle répartit les tâches de façon conforme à la structure exigée :
o	Proposal, SOTA, Methodology, Experiments, Results, Discussion.
________________________________________
6. Version ultra courte pour le rapport (Teamwork section)
Personne A : responsable du pipeline de restauration d’image
(modèles, datasets, entraînement, production des images restaurées).
Personne B : responsable du pipeline OCR et de l’évaluation
(metrics, OCR pipeline, analyse quantitative et qualitative).
Les deux ont travaillé en parallèle pour éviter toute dépendance bloquante.
La fusion finale combine les images restaurées et les résultats OCR pour une analyse complète.



























Répartition du State of the Art (3–5 pages) — 100 pour cent parallèle
Le SOTA doit couvrir deux domaines distincts mais complémentaires :
1.	La restauration d’image (défloutage)
2.	L’OCR + les métriques de qualité
3.	Les datasets utilisés
4.	La synthèse finale + les limites / faiblesses des approches existantes
Ces parties sont structurellement indépendantes, donc chacun peut écrire sa partie sans attendre l’autre.
________________________________________
Personne A — State of the Art sur : Défloutage et restauration d’image
Objectif : couvrir tout ce qui concerne la vision par ordinateur pure.
A écrit :
1. Méthodes classiques de défloutage
•	Déconvolution aveugle
•	Wiener filtering
•	Lucy–Richardson
•	Limitations (artefacts, instabilité)
2. Méthodes deep learning modernes
•	DeblurGAN / DeblurGAN-v2
•	MPRNet
•	U-Net et variantes
•	SRN (Scale-Recurrent Networks)
•	Approches multi-échelle / multi-patch
3. Avantages / limites des méthodes existantes
Exemples :
•	GANs produisent des effets réalistes mais parfois instables
•	CNNs classiques perdent les traits fins du texte
•	Modèles récents manquent parfois de généralisation
•	Peu de modèles sont optimisés pour texte et pas seulement pour scènes générales
A rédige tout cela sans dépendre de B.
________________________________________
Personne B — State of the Art sur : OCR, métriques et chaîne d’évaluation
Objectif : couvrir tout ce qui concerne la reconnaissance de texte et son évaluation.
B écrit :
1. OCR modernes
•	Tesseract (historique, limites, pipeline classique)
•	PaddleOCR (state-of-the-art open source)
•	CRNN + CTC
•	Transformers pour OCR
•	Approches end-to-end vision → texte
2. Impact du flou et du bruit sur OCR
•	Études montrant dégradation du CER
•	Sensibilité des traits fins
•	Problème des caractères joints ou déformés
3. Métriques de comparaison
•	PSNR / SSIM pour la qualité visuelle
•	CER / WER pour la qualité textuelle
•	Pourquoi l’OCR est indispensable pour évaluer un modèle de déblurring orienté texte
4. Limites des OCR actuels
•	Fragiles au flou motion blur
•	Mauvaise segmentation des caractères
•	Pas optimisés pour images très bruitées
B rédige tout cela sans dépendre de A.
________________________________________
Partie commune — Rédigée ensemble (mais courte)
Cette section finale ne dépend d’aucune partie technique du code et peut être rédigée à tout moment, même en début de projet.
Vous écrivez ensemble :
1. Datasets existants pour texte et défloutage
•	RealBlur
•	ICDAR
•	SynthText
•	Avantages / limites
•	Pourquoi ils conviennent à votre projet
2. Synthèse critique
Répond aux attentes du prof :
•	Quelles sont les lacunes des méthodes actuelles ?
•	Pourquoi un modèle spécialisé pour les textes est nécessaire ?
•	Pourquoi l’intégration OCR + défloutage est originale ?
3. Conclusion du SOTA
•	Justifie parfaitement votre projet
•	Fait le lien avec les sections Méthodologie / Motivation du rapport final

