from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from cinema.models import Film, Session
from gallery_seo.forms import ImageFormSet, GalleryForm, SeoForm
from gallery_seo.models import Image
from .forms import NewsPromoForm, PagesForm, ContactCollectionForm, ContactFormSet
from .models import News_promo, Page, Contact_page, Contact_collection


def film_page(request, film_id):
	pages = get_object_or_404(Film, id=film_id)
	gallery_qs = Image.objects.filter(galleryId=pages.gallery.pk)
	image_form_set = ImageFormSet(queryset=gallery_qs)
	seo_form = SeoForm(instance=pages.seo)
	# x = 'json_form': " ".join(str(x) for x in obj.positions)
	session = Session.objects.filter(film_id=film_id)
	print(session)
	context = {"pages": Page.objects.all(),
	           'page_form': pages,
	           'seo_form': seo_form,
	           'images_formset': image_form_set}
	return render(request, 'pages/film.html', context)


# Create your views here.
@login_required(login_url='Login')
def news(request):
	news = News_promo.objects.filter(type='News')
	context = {'news': news}
	return render(request, 'pages/news.html', context)


@login_required(login_url='Login')
def delete_news_promo(request, news_promo_id):
	news_promo = News_promo.objects.get(id=news_promo_id)
	if news_promo.type == 'News':
		news_promo.delete()
		return redirect('news')
	news_promo.delete()
	return redirect('promos')


@login_required(login_url='Login')
def add_news_promo(request, form_type):
	if request.method == 'POST':
		print(request.POST)
		news_promo_form = NewsPromoForm(request.POST, request.FILES)
		seo_form = SeoForm(request.POST)
		image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())

		if all([seo_form.is_valid(), news_promo_form.is_valid(), image_form_set.is_valid()]):
			print("if")
			seo = seo_form.save(commit=False)
			seo.save()
			news_promo = news_promo_form.save(commit=False)
			images = image_form_set.save(commit=False)
			gallery = GalleryForm().save(commit=False)
			gallery.save()
			news_promo.seo = seo
			for image in images:
				if image.image:
					image.galleryId = gallery
					image.save()

			news_promo.gallery = gallery
			news_promo.save()
			# print(request.POST, request.FILES)
			if form_type == 'News':
				return redirect('news')
			else:
				return redirect('promos')
	else:
		# print('not valid')
		news_promo_form = NewsPromoForm(initial={'type': form_type, 'active': True})
		seo_form = SeoForm()
		image_form_set = ImageFormSet(queryset=Image.objects.none())
	return render(request, 'pages/add_news_promo.html', {'news_promo_form': news_promo_form,
	                                                     'seo_form': seo_form, 'images_formset': image_form_set})


@login_required(login_url='Login')
def news_promo_update(request, news_promo_id):
	obj = get_object_or_404(News_promo, id=news_promo_id)
	gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
	if request.method == 'POST':
		news_promo_form = NewsPromoForm(request.POST, request.FILES or None, instance=obj)
		image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
		seo_form = SeoForm(request.POST, instance=obj.seo)
		print(request.POST, request.FILES)
		if all([news_promo_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
			seo = seo_form.save(commit=False)
			seo.save()
			news_promo = news_promo_form.save(commit=False)
			images = image_form_set.save(commit=False)
			news_promo.seo = seo
			for del_image in image_form_set.deleted_objects:
				print(del_image)
				del_image.delete()
			for image in images:
				if image.image:
					image.galleryId = news_promo.gallery
					image.save()
			news_promo.save()
			print(request.POST, request.FILES)
			if news_promo.type == 'News':
				return redirect('news')
			else:
				return redirect('promos')
	else:
		print('no valid')
		image_form_set = ImageFormSet(queryset=gallery_qs)
		news_promo_form = NewsPromoForm(instance=obj)
		seo_form = SeoForm(instance=obj.seo)

	context = {'news_promo_form': news_promo_form, 'images_formset': image_form_set, 'seo_form': seo_form}
	return render(request, 'pages/news_promo_update.html', context)


@login_required(login_url='Login')
def promos(request):
	obj_promos = News_promo.objects.filter(type='Promo')
	context = {'promos': obj_promos}
	return render(request, 'pages/promos.html', context)


def page(request, page_id):
	pages = get_object_or_404(Page, id=page_id)
	gallery_qs = Image.objects.filter(galleryId=pages.gallery.pk)
	image_form_set = ImageFormSet(queryset=gallery_qs)
	seo_form = SeoForm(instance=pages.seo)

	context = {"pages": Page.objects.all(),
	           'page_form': pages,
	           'seo_form': seo_form,
	           'images_formset': image_form_set}
	return render(request, 'pages/page.html', context)


@login_required(login_url='Login')
def pages(request):
	obj_pages = Page.objects.all()
	context = {'pages': obj_pages}
	return render(request, 'pages/pages.html', context)


@login_required(login_url='Login')
def add_page(request):
	if request.method == 'POST':
		other_page_form = PagesForm(request.POST, request.FILES)
		# print(type(other_page_form))
		seo_form = SeoForm(request.POST)  # , prefix="seo"
		image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
		# print(request.POST, request.FILES)
		if all([seo_form.is_valid(), other_page_form.is_valid(), image_form_set.is_valid()]):
			seo = seo_form.save(commit=False)
			seo.save()
			other_page = other_page_form.save(commit=False)
			images = image_form_set.save(commit=False)
			gallery = GalleryForm().save(commit=False)
			gallery.save()
			other_page.seo = seo
			for image in images:
				if image.image:
					image.galleryId = gallery
					image.save()

			other_page.gallery = gallery
			other_page.save()
			# print(request.POST, request.FILES)
			return redirect('pages')
	else:
		print('not valid')
		other_page_form = PagesForm()
		seo_form = SeoForm()
		image_form_set = ImageFormSet(queryset=Image.objects.none())
	context = {'other_page_form': other_page_form, 'images_formset': image_form_set, 'seo_form': seo_form}
	return render(request, 'pages/add_update_page.html', context)


@login_required(login_url='Login')
def update_page(request, page_id):
	obj_page = get_object_or_404(Page, id=page_id)
	gallery_qs = Image.objects.filter(galleryId=obj_page.gallery.pk)
	if request.method == 'POST':
		other_page_form = PagesForm(request.POST, request.FILES or None, instance=obj_page)
		image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
		seo_form = SeoForm(request.POST, instance=obj_page.seo)
		# print(request.POST, request.FILES)
		if all([other_page_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
			seo = seo_form.save(commit=False)
			seo.save()
			print(request.POST)
			other_page = other_page_form.save(commit=False)
			images = image_form_set.save(commit=False)
			other_page.seo = seo
			for del_image in image_form_set.deleted_objects:
				# print(del_image)
				del_image.delete()
			for image in images:
				if image.image:
					image.galleryId = other_page.gallery
					image.save()
			other_page.save()
			# print(request.POST, request.FILES)
			return redirect('pages')
	else:
		# print('no valid')
		image_form_set = ImageFormSet(queryset=gallery_qs)
		other_page_form = PagesForm(instance=obj_page)
		seo_form = SeoForm(instance=obj_page.seo)

	context = {'other_page_form': other_page_form, 'images_formset': image_form_set, 'seo_form': seo_form}
	return render(request, 'pages/add_update_page.html', context)


@login_required(login_url='Login')
def delete_page(request, page_id):
	del_page = Page.objects.get(id=page_id)
	del_page.delete()
	return redirect('pages')


@login_required(login_url='Login')
def contact_page(request):
	obj_collection = get_object_or_404(Contact_collection, id=1)
	contacts_qs = Contact_page.objects.filter(contact_collection_id=1)
	if request.method == 'POST':
		contact_collection_form = ContactCollectionForm(request.POST, instance=obj_collection)
		seo_form = SeoForm(request.POST, instance=obj_collection.seo)
		contact_formset = ContactFormSet(request.POST, request.FILES or None,
		                                 queryset=contacts_qs)
		print(request.POST, request.FILES)
		if all([contact_formset.is_valid(), contact_collection_form.is_valid(), seo_form.is_valid()]):
			contact_collection = contact_collection_form.save(commit=False)
			contacts = contact_formset.save(commit=False)
			seo = seo_form.save(commit=False)
			seo.save()
			contact_collection.seo = seo
			contact_collection.save()
			for contact in contacts:
				contact.contact_collection = contact_collection
				contact.save()
			print('Data saved')
			return redirect('pages')
	else:
		print('not valid')
		contact_collection_form = ContactCollectionForm(instance=obj_collection)
		seo_form = SeoForm(instance=obj_collection.seo)
		contact_formset = ContactFormSet(queryset=contacts_qs)
	context = {'contact_collection_form': contact_collection_form,
	           'seo_form': seo_form, 'contact_formset': contact_formset}
	return render(request, 'pages/contact_page.html', context)
