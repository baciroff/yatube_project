from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')

def group_posts(request, slug):
    return HttpResponse(f'{slug}'
                        f'Lorem Ipsum - это текст-"рыба", часто используемый '
                        f'в печати и вэб-дизайне. Lorem Ipsum является '
                        f'стандартной "рыбой" для текстов на латинице с '
                        f'начала XVI века. В то время некий безымянный '
                        f'печатник создал большую коллекцию размеров и форм '
                        f'шрифтов, используя Lorem Ipsum для распечатки '
                        f'образцов. Lorem Ipsum не только успешно пережил '
                        f'без заметных изменений пять веков, но и перешагнул '
                        f'в электронный дизайн. Его популяризации в новое '
                        f'время послужили публикация листов Letraset с '
                        f'образцами Lorem Ipsum в 60-х годах и, в более '
                        f'недавнее время, программы электронной вёрстки типа '
                        f'Aldus PageMaker, в шаблонах которых используется '
                        f'Lorem Ipsum.')
