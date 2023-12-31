# Generated by Django 4.2.5 on 2023-09-09 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_category_parent_order_user_orderitem_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='store.category', verbose_name='دسته بندی'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='عکس محصول'),
        ),
        migrations.AlterField(
            model_name='product',
            name='selled_count',
            field=models.IntegerField(default=0, verbose_name='تعداد فروش'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=0, verbose_name='موجودی محصول'),
        ),
    ]
