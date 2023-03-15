from django.shortcuts import render, redirect, get_object_or_404
from .models import Film, Hall, Cinema
from .forms import FilmForm, CinemaForm, HallForm, PositionForm
from gallery_seo.forms import SeoForm, GalleryForm, ImageFormSet
from gallery_seo.forms import Image
from django.contrib.auth.decorators import login_required
from json import decoder


# Create your views here.

def index(request):
    return render(request, 'layout/basic.html')


def buy(request, film_id):
    film = get_object_or_404(Film, id=film_id)
    obj = get_object_or_404(Hall, id=film.pk)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)

    if request.method == 'POST':
        hall_form = HallForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo)
    else:
        image_form_set = ImageFormSet(queryset=gallery_qs)
        hall_form = HallForm(instance=obj)
        seo_form = SeoForm(instance=obj.seo)
    # print(request.POST)
    print(obj.positions)
    context = {'film': film,
                'hall_form': hall_form,
               'seo_form': seo_form,
               'images_formset': image_form_set,
               'json_form': obj.positions
               }
    return render(request, 'cinema/schedulbuy.html', context)


@login_required(login_url='Login')
def films(request):
    films = Film.objects.all()
    context = {"films": films}
    return render(request, 'cinema/films.html', context)
    # date = datetime.date.today()
    # films_now = Film.objects.filter(date__lte=date)
    # films_soon = Film.objects.filter(date__gt=date).order_by('date')[:5]
    # context = {"films": films_now, 'films_soon': films_soon}
    # return render(request, 'cinema/films.html', context)


@login_required(login_url='Login')
def add_film(request):
    if request.method == 'POST':
        seo_form = SeoForm(request.POST)
        # print(request.POST)
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        film_form = FilmForm(request.POST, request.FILES)

        # print(request.POST, '\n', request.FILES)
        if all([film_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            film = film_form.save(commit=False)
            images = image_form_set.save(commit=False)
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            film.seo = seo

            for image in images:
                if image.image:
                    image.galleryId = gallery
                    image.save()

            film.gallery = gallery
            film.save()
            # print(request.POST, request.FILES)
            return redirect('films')
    else:
        # print('no valid')
        image_form_set = ImageFormSet(queryset=Image.objects.none())
        film_form = FilmForm()
        seo_form = SeoForm()
    return render(request, 'cinema/film_create.html', {'film_form': film_form, 'seo_form': seo_form,
                                                       'images_formset': image_form_set})


@login_required(login_url='Login')
def film_update(request, film_id):
    obj = get_object_or_404(Film, id=film_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
    if request.method == 'POST':
        film_form = FilmForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo)
        # print(request.POST, request.FILES)
        if all([film_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            film = film_form.save(commit=False)
            images = image_form_set.save(commit=False)
            film.seo = seo
            # print(image_form_set.deleted_objects)
            for del_image in image_form_set.deleted_objects:
                # print(del_image)
                del_image.delete()

            for image in images:
                if image.image:
                    image.galleryId = film.gallery
                    image.save()
            film.save()
            # print(request.POST, request.FILES)
            return redirect('films')
    else:
        # print('no valid')
        image_form_set = ImageFormSet(queryset=gallery_qs)
        film_form = FilmForm(instance=obj)
        seo_form = SeoForm(instance=obj.seo)
    return render(request, 'cinema/film_update.html', {'film_form': film_form, 'seo_form': seo_form,
                                                       'images_formset': image_form_set,
                                                       })


@login_required(login_url='Login')
def add_cinema(request):
    # print(request.POST, request.FILES)
    if request.method == 'POST':
        # hall_form_set = HallFormSet(request.POST, queryset=Hall.objects.none())
        seo_form = SeoForm(request.POST)
        cimena_form = CinemaForm(request.POST, request.FILES)
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        if all([seo_form.is_valid(), cimena_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            cimena = cimena_form.save(commit=False)
            images = image_form_set.save(commit=False)
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            cimena.seo = seo
            for image in images:
                if image.image:
                    image.galleryId = gallery
                    image.save()

            cimena.gallery = gallery
            cimena.save()
            # print(request.POST, request.FILES)
            return redirect('cinemas')

    else:
        # print('not valid')
        # print(request.POST, request.FILES)
        seo_form = SeoForm()
        cimena_form = CinemaForm()
        image_form_set = ImageFormSet(queryset=Image.objects.none())
        # hall_form_set = HallFormSet(queryset=Hall.objects.none())
    context = {'cinema_form': cimena_form, 'images_formset': image_form_set, 'seo_form': seo_form}

    return render(request, 'cinema/cinema_create.html', context)


@login_required(login_url='Login')
def cinemas(request):
    cinemas = Cinema.objects.all()
    context = {"cinemas": cinemas}
    return render(request, 'cinema/cinemas.html', context)


@login_required(login_url='Login')
def cinema_update(request, cinema_id):
    obj = get_object_or_404(Cinema, id=cinema_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)
    halls = Hall.objects.filter(cinema_id=cinema_id)
    if request.method == 'POST':
        cinema_form = CinemaForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo)
        # print(request.POST)
        if all([cinema_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            cinema = cinema_form.save(commit=False)
            images = image_form_set.save(commit=False)
            cinema.seo = seo
            for del_image in image_form_set.deleted_objects:
                # print(del_image)
                del_image.delete()

            for image in images:
                if image.image:
                    image.galleryId = cinema.gallery
                    image.save()
            cinema.save()
            # print(request.POST)
            return redirect('cinemas')
    else:
        # print('no valid')
        image_form_set = ImageFormSet(queryset=gallery_qs)
        cinema_form = CinemaForm(instance=obj)
        seo_form = SeoForm(instance=obj.seo)

    context = {'cinema_form': cinema_form,
               'seo_form': seo_form,
               'images_formset': image_form_set,
               'halls': halls}
    return render(request, 'cinema/cinema_update.html', context)


@login_required(login_url='Login')
def add_hall(request, cinema_id):
    if request.method == 'POST':
        hall_form = HallForm(request.POST, request.FILES)
        seo_form = SeoForm(request.POST)
        image_form_set = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())
        # print(request.POST, request.FILES)
        if all([seo_form.is_valid(), hall_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            hall = hall_form.save(commit=False)
            list_pos = str(request.POST['position_id']).replace(".", " ").replace(",", " ").replace("  ", " ").split(" ")
            nums = 0
            for num in list_pos:
                try:
                    list_pos[nums] = int(num)
                    nums += 1
                except ValueError:
                    list_pos.pop(nums)

            hall.positions = list_pos
            images = image_form_set.save(commit=False)
            gallery = GalleryForm().save(commit=False)
            gallery.save()
            hall.seo = seo
            hall.cinema = Cinema.objects.get(pk=cinema_id)
            for image in images:
                if image.image:
                    image.galleryId = gallery
                    image.save()

            hall.gallery = gallery
            hall.save()
            # print(request.POST, request.FILES)
            return redirect('cinema_update', cinema_id)
    else:
        hall_form = HallForm()
        seo_form = SeoForm()
        image_form_set = ImageFormSet(queryset=Image.objects.none())
    context = {'hall_form': hall_form, 'images_formset': image_form_set, 'seo_form': seo_form}
    return render(request, 'cinema/hall_create.html', context)


@login_required(login_url='Login')
def hall_update(request, cinema_id, hall_id):
    obj = get_object_or_404(Hall, id=hall_id)
    gallery_qs = Image.objects.filter(galleryId=obj.gallery.pk)

    if request.method == 'POST':
        hall_form = HallForm(request.POST, request.FILES or None, instance=obj)
        image_form_set = ImageFormSet(request.POST, request.FILES or None, queryset=gallery_qs)
        seo_form = SeoForm(request.POST, instance=obj.seo)

        position = str(request.POST['position_id']).replace(".", " ").replace(",", " ").replace("  ", " ")
        list_pos = position.split(" ")
        nums = 0
        for num in list_pos:
            try:
                list_pos[nums] = int(num)
                nums += 1
            except ValueError:
                list_pos.pop(nums)

        obj.positions = list_pos
        obj.save()

        if all([hall_form.is_valid(), seo_form.is_valid(), image_form_set.is_valid()]):
            seo = seo_form.save(commit=False)
            seo.save()
            hall = hall_form.save(commit=False)
            images = image_form_set.save(commit=False)
            hall.seo = seo
            for del_image in image_form_set.deleted_objects:
                # print(del_image)
                del_image.delete()
            for image in images:
                if image.image:
                    image.galleryId = hall.gallery
                    image.save()
            hall.save()
            # print(request.POST, request.FILES)
            return redirect('cinema_update', cinema_id)
    else:
        image_form_set = ImageFormSet(queryset=gallery_qs)
        hall_form = HallForm(instance=obj)
        seo_form = SeoForm(instance=obj.seo)
    # print(request.POST)
    print(obj.positions)
    context = {'hall_form': hall_form,
               'seo_form': seo_form,
               'images_formset': image_form_set,
               'json_form': " ".join(str(x) for x in obj.positions),
               }
    return render(request, 'cinema/hall_update.html', context)


@login_required(login_url='Login')
def delete_hall(request, hall_id, cinema_id):
    hall = Hall.objects.get(id=hall_id)
    hall.delete()
    return redirect('cinema_update', cinema_id)


