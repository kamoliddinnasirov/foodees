from django.db import models



class Home(models.Model):
    banner = models.ImageField(upload_to='media/banner/%Y/%m/%d')
    title = models.CharField(max_length=25)


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = 'Homes'



class About(models.Model):
    left_image = models.ImageField(upload_to='about/left_image/%Y/%m/%d', blank=True)
    about_title = models.CharField(max_length=255, blank=True)
    descriptions = models.TextField(blank=True)
    article = models.CharField(max_length=255, blank=True)
    article_author = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return self.about_title
    
    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'
    



class Feature(models.Model):
    icons = models.ImageField(upload_to='Feature/icons/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=25, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)


    def __str__(self) -> str:
        return self.title
    

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'



class Menu_Category(models.Model):
    icons = models.ImageField(upload_to='Menu_Category/icons/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=255, blank=True)



    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Menu(models.Model):
    icons = models.ImageField(upload_to='Menu/icons/%Y/%m/%d', blank=True)
    title = models.CharField(max_length=25, blank=True)
    sub_title = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Menu_Category, on_delete = models.CASCADE, blank=True)
    food_name = models.CharField(max_length=255, blank=True)
    food_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    food_image = models.ImageField(upload_to='Menu/food_image/%Y/%m/%d', blank=True)



    def __str__(self) -> str:
        return self.title
    


    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menues'


