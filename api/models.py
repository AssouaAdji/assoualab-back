from django.db import models

class History(models.Model):
    year = models.DateField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # category
    client = models.CharField(max_length=255)
    date = models.DateField()
    # tech = models.

# {
# 				id: 1,
# 				title: "Plateforme E-commerce",
# 				description:
# 					"Solution complète avec paiement sécurisé et gestion de stock",
# 				category: "web",
# 				image: "https://via.placeholder.com/600x400?text=E-commerce",
# 				details: {
# 					client: "FashionStore",
# 					date: "Janvier 2023",
# 					technologies: ["React", "Node.js", "MongoDB", "Stripe"],
# 					description:
# 						"Développement d'une plateforme e-commerce complète avec système de recommandation personnalisé et tableau de bord administrateur.",
# 				},
# 			},