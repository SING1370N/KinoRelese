from django.contrib.auth.decorators import login_required
from gallery_seo.forms import SeoForm, GalleryForm, ImageFormSet
from gallery_seo.forms import Image
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BannerForm, BannerCollectionForm, BackgroundBannerForm, BannerFormSet, BannerNewsCollectionForm, \
    BannerNewsFormSet
from .models import Banner, Banner_collection, Background_banner, Banner_news, Banner_news_collection
from django.forms import modelformset_factory, inlineformset_factory


# @login_required(login_url='Login')
# def baners(request):
#     if request.method == 'POST':
#         seo_form = SeoForm(request.POST)
#         # print(request.POST)
#         image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
#         print(image_form_set)
#         # film_form = FilmForm(request.POST, request.FILES)
#
#         # print(request.POST, '\n', request.FILES)
#         # if all([film_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
#         #     seo = seo_form.save(commit=False)
#         #     seo.save()
#         #     # film = film_form.save(commit=False)
#         #     images = image_form_set.save(commit=False)
#         #     gallery = GalleryForm().save(commit=False)
#         #     gallery.save()
#         #     film.seo = seo
#         #
#         #     for image in images:
#         #         if image.image:
#         #             image.galleryId = gallery
#         #             image.save()
#         #
#         #     film.gallery = gallery
#         #     film.save()
#         #     print(request.POST, request.FILES)
#         #     return redirect('films')
#     else:
#         # print('no valid')
#         image_form_set = ImageFormSet(queryset=Image.objects.none())
#         # film_form = FilmForm()
#         seo_form = SeoForm()
#     return render(request, 'banners/banner.html', {'images_formset': image_form_set})

# Create your views here.
def baners(request):
    print("BANNERS")
    obj_banner = get_object_or_404(Banner_collection, id=1)
    obj_back_banner = get_object_or_404(Background_banner, id=1)
    obj_banner_news = get_object_or_404(Banner_news_collection, id=1)
    print("BAN:", obj_banner, obj_back_banner, obj_banner_news)
    qs_banners = Banner.objects.filter(banner_collection_id=1)
    qs_news_banners = Banner_news.objects.filter(banner_news_collection_id=1)
    background_banner_form = BackgroundBannerForm(request.POST, request.FILES, instance=obj_back_banner)
    banner_formset = BannerFormSet(request.POST, request.FILES,
                                   queryset=qs_banners)
    banner_collection_form = BannerCollectionForm(request.POST, instance=obj_banner)
    banner_news_collection_form = BannerNewsCollectionForm(request.POST, instance=obj_banner_news)
    banner_news_formset = BannerNewsFormSet(request.POST, request.FILES, queryset=qs_news_banners)
    print(request.POST, request.FILES)
    if request.POST.get('form_type') == 'banners_form':
        print('banners_form')
        print(request.POST, request.FILES)
        if all([banner_formset.is_valid(), banner_collection_form.is_valid()]):
            banner_collection = banner_collection_form.save(commit=False)
            banners = banner_formset.save(commit=False)
            for del_banner in banner_formset.deleted_objects:
                print(del_banner)
                del_banner.delete()

            for banner in banners:
                banner.banner_collection = banner_collection
                banner.save()
            banner_collection.save()
            print('Data saved')
            return redirect('banners')

        else:
            print('Not valid')

    if request.POST.get('form_type') == 'back_banner_form':
        print('back_banner_form')
        if background_banner_form.is_valid():
            background_banner = background_banner_form.save(commit=False)
            background_banner.save()
            print('Data saved')
            return redirect('banners')
        else:
            print('Not valid')

    if request.POST.get('form_type') == 'banners_news_form':
        print('banners_news_form')
        # print(request.POST, request.FILES)
        if all([banner_news_formset.is_valid(), banner_news_collection_form.is_valid()]):
            banner_news_collection = banner_news_collection_form.save(commit=False)
            banners_news = banner_news_formset.save(commit=False)
            for del_news_banner in banner_news_formset.deleted_objects:
                print(del_news_banner)
                del_news_banner.delete()
            for banner_news in banners_news:
                banner_news.banner_news_collection = banner_news_collection
                banner_news.save()
            banner_news_collection.save()
            print('Data saved')
            return redirect('banners')

        else:
            print('Not valid')

    else:
        banner_news_collection_form = BannerNewsCollectionForm(instance=obj_banner_news)
        banner_news_formset = BannerNewsFormSet(queryset=qs_news_banners)
        background_banner_form = BackgroundBannerForm(instance=obj_back_banner)
        banner_formset = BannerFormSet(queryset=qs_banners)
        banner_collection_form = BannerCollectionForm(instance=obj_banner)

    context = {'banner_collection_form': banner_collection_form,
               'formset': banner_formset, 'background_banner_form': background_banner_form,
               'banner_news_formset': banner_news_formset, 'banner_news_collection_form': banner_news_collection_form}
    return render(request, 'banners/banner.html', context)
