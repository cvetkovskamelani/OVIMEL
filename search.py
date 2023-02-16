from collections import deque
import heapq


def breadth_first_search_find_path(graph, starting_vertex, goal_vertex, verbose=False):
    """
    Returns the path from starting_vertex to goal_vertex using the DFS algorithm.
    """
    # Ако почетниот јазол е еднаков на целниот, тогаш нема логика да пребаруваме воопшто
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return []
    # Користиме листа на посетени јазли која всушност е податочна структура множество. 
    # За посетен јазол го сметаме оној јазол кој ќе го истражиме како сосед на јазолот кој го разгрануваме.
    visited = {starting_vertex}
    # Користиме двојно поврзана листа која ни е редицата од која ќе го земаме следниот јазол за разгранување.
    # Тука ја памтиме и моменталната патека за секој јазол од почетниот.
    queue = deque([[starting_vertex]])
    # Пребаруваме сѐ додека има јазли за разгранување во редицата.
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
        # Членови на редицата јазли се патеките од почетниот јазол до некој јазол кој треба да се разграни.
        # За да го земаме наредниот јазол за разгранување, 
        #    ние треба од редицата да ја извадиме патеката на тој јазол.
        vertex_list = queue.popleft()
        # Јазолот за разгранување е послениот во оваа листа.
        vertex_to_expand = vertex_list[-1]
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex_to_expand))
        # Го разгрануваме така што пребаруваме низ сите негови соседи.
        for neighbour in graph.neighbours(vertex_to_expand):
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
                # Ако некој сосед не е посетен, тогаш го додаваме во листата на посетени, 
                #     и во редицата на јазли за разгранување.
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex_to_expand))
                # Тука ја вршиме проверката дали сме стигнале до целниот јазол 
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {}'
                              .format(neighbour, vertex_list + [neighbour]))
                    return vertex_list + [neighbour]
                visited.add(neighbour)
                # Бидејќи ова е пребарување прво по широчина, 
                #     соседот го додаваме на крајот од редицата јазли за разгранување.
                # Соседот го врзуваме со патеката од почетниот јазол до моменталниот кој го разгрануваме.
                queue.append(vertex_list + [neighbour])
        if verbose:
            print()


def depth_first_search_find_path(graph, starting_vertex, goal_vertex, verbose=False):
    """
    Returns the path from starting_vertex to goal_vertex using the BFS algorithm.
    """
    # Ако почетниот јазол е еднаков на целниот, тогаш нема логика да пребаруваме воопшто
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return []
    # Користиме листа на посетени јазли која всушност е податочна структура множество. 
    # За посетен јазол го сметаме оној јазол кој ќе го истражиме како сосед на јазолот кој го разгрануваме.
    visited = {starting_vertex}
    # Користиме двојно поврзана листа која ни е редицата од која ќе го земаме следниот јазол за разгранување.
    # Тука ја памтиме и моменталната патека за секој јазол од почетниот.
    queue = deque([[starting_vertex]])
    # Пребаруваме сѐ додека има јазли за разгранување во редицата.
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
        # Членови на редицата јазли се патеките од почетниот јазол до некој јазол кој треба да се разграни.
        # За да го земаме наредниот јазол за разгранување, 
        #    ние треба од редицата да ја извадиме патеката на тој јазол.
        vertex_list = queue.popleft()
        # Јазолот за разгранување е послениот во оваа листа.
        vertex_to_expand = vertex_list[-1]
        if verbose:
            print('Го разгрануваме јазолот {}'.format(vertex_to_expand))
        # Го разгрануваме така што пребаруваме низ сите негови соседи.
        for neighbour in graph.neighbours(vertex_to_expand):
            if neighbour in visited:
                if verbose:
                    print('{} е веќе посетен'.format(neighbour))
            else:
                # Ако некој сосед не е посетен, тогаш го додаваме во листата на посетени, 
                #     и во редицата на јазли за разгранување.
                if verbose:
                    print('{}, кој е соседен јазол на {} го немаме посетено до сега, затоа го додаваме во редот '
                          'за разгранување и го означуваме како посетен'.format(neighbour, vertex_to_expand))
                # Тука ја вршиме проверката дали сме стигнале до целниот јазол 
                if neighbour == goal_vertex:
                    if verbose:
                        print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {}'
                              .format(neighbour, vertex_list + [neighbour]))
                    return vertex_list + [neighbour]
                visited.add(neighbour)
                # Бидејќи ова е пребарување прво по длабочина, 
                #     соседот го додаваме на почетокот од редицата јазли за разгранување.
                # Соседот го врзуваме со патеката од почетниот јазол до моменталниот кој го разгрануваме.
                queue.appendleft(vertex_list + [neighbour])
        if verbose:
            print()


def uniform_cost_search(graph, starting_vertex, goal_vertex, verbose=False):
    """
    Returns the path from starting_vertex to goal_vertex using the uniform-cost algorithm.
    """
    # Ако почетниот јазол е еднаков на целниот, тогаш нема логика да пребаруваме воопшто
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return
    # Користиме множество на разгранети јазли. 
    # За разгранет јазол го сметаме оној јазол на кој ќе му ги истражиме и испроцесираме соседите.
    expanded = set()
    # Користиме листа која ни е подредена редица од која ќе го земаме следниот јазол за разгранување.
    # Тука ја памтиме и моменталната патека за секој јазол од почетниот. Дополнително, ја памтиме и цената на патот до тој момент.
    # Редицата ја преуредуваме на специјален начин така што ќе ја направиме хип структура (анг. heap).
    # Понатаму, со редицата ќе работиме само преку heapq библиотеката.
    queue = [(0, [starting_vertex])]
    heapq.heapify(queue)
    # Пребаруваме сѐ додека има јазли за разгранување во редицата.
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
        # Членови на редицата јазли се патеките од почетниот јазол до некој јазол кој треба да се разграни.
        # За да го земеме наредниот јазол за разгранување, ние треба од редицата да ја извадиме патеката на тој јазол.
        weight, vertex_list = heapq.heappop(queue)
        # Јазолот за разгранување е последниот во оваа листа.
        vertex_to_expand = vertex_list[-1]
        # Тука ја вршиме проверката дали сме стигнале до целниот јазол.
        if vertex_to_expand == goal_vertex:
            if verbose:
                print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {} со цена {}'
                      .format(vertex_to_expand, vertex_list, weight))
            return weight, vertex_list
        # Ако веќе сме го разграниле овој јазол, нема логика да го разгрануваме пак.
        if vertex_to_expand in expanded:
            if verbose:
                print('{} е веќе разгранет'.format(vertex_to_expand, weight, vertex_list))
            continue
        if verbose:
            print('Го разгрануваме јазолот {} од ({}, {})'.format(vertex_to_expand, weight, vertex_list))
        # На оваа линија код, сигурни сме дека не сме го разграниле моменталниот јазол. Го разгрануваме така што пребаруваме низ сите негови соседи.
        for neighbour, new_weight in graph.neighbours(vertex_to_expand):
            if neighbour in expanded:
                if verbose:
                    print('{} е веќе разгранет'.format(neighbour))
            else:
                # Ако моменталниот сосед не е разгранет, го додаваме во редицата на јазли за разгранување.
                if verbose:
                    print('{} со тежина {}, кој е соседен јазол на {}, го додаваме во редот за разгранување со нова '
                          'цена и го означуваме како разгранет'.format(neighbour, new_weight, vertex_to_expand))
                # Бидејќи ова е пребарување со униформна цена, соседот кој го додаваме ќе биде соодветно додаден преку библиотеката heapq.
                heapq.heappush(queue, (weight + new_weight, vertex_list + [neighbour]))
        # Откако го разгранивме јазолот, го додаваме во множеството разгранети јазли.
        expanded.add(vertex_to_expand)
        if verbose:
            print()


def a_star_search(graph, starting_vertex, goal_vertex, heuristic_function, alpha=1, verbose=False):
    """
    Returns the path from starting_vertex to goal_vertex using the A-star search algorithm.
    """
    # Ако почетниот јазол е еднаков на целниот, тогаш нема логика да пребаруваме воопшто
    if starting_vertex == goal_vertex:
        if verbose:
            print('Почетниот и бараниот јазол се исти')
        return
    # Користиме множество на разгранети јазли. 
    # За разгранет јазол го сметаме оној јазол на кој ќе му ги истражиме и испроцесираме соседите.
    expanded = set()
    # Користиме листа која ни е подредена редица од која ќе го земаме следниот јазол за разгранување.
    # Тука ја памтиме и моменталната патека за секој јазол од почетниот. Дополнително, ја памтиме и цената на патот до тој момент.
    # Редицата ја преуредуваме на специјален начин така што ќе ја направиме хип структура (анг. heap).
    # Понатаму, со редицата ќе работиме само преку heapq библиотеката.
    queue = [((0, 0), [starting_vertex])]
    heapq.heapify(queue)
    # Пребаруваме сѐ додека има јазли за разгранување во редицата.
    while queue:
        if verbose:
            print('Ред за разгранување:')
            for element in queue:
                print(element, end=' ')
            print()
            print()
        # Членови на редицата јазли се патеките од почетниот јазол до некој јазол кој треба да се разграни.
        # За да го земеме наредниот јазол за разгранување, ние треба од редицата да ја извадиме патеката на тој јазол.
        weight_tuple, vertex_list = heapq.heappop(queue)
        # Во оваа имплементација на А-ѕвезда користиме торка од две тежини каде редицата ја подредуваме по збирот 
        # на тежината на поминатиот пат и дојавата. Подредуваме по тежината current_a_star_weight која не ни треба понатаму.
        # Понатаму ја користиме само тежината current_path_weight.
        current_a_star_weight, current_path_weight = weight_tuple
        # Јазолот за разгранување е последниот во оваа листа.
        vertex_to_expand = vertex_list[-1]
        # Тука ја вршиме проверката дали сме стигнале до целниот јазол.
        if vertex_to_expand == goal_vertex:
            if verbose:
                print('Го пронајдовме посакуваниот јазол {}. Патеката да стигнеме до тука е {} со цена {}'
                      .format(vertex_to_expand, vertex_list, current_path_weight))
            return current_path_weight, vertex_list
        # Ако веќе сме го разграниле овој јазол, нема логика да го разгрануваме пак.
        if vertex_to_expand in expanded:
            if verbose:
                print('{} е веќе разгранет'.format(vertex_to_expand, current_path_weight, vertex_list))
            continue
        if verbose:
            print('Го разгрануваме јазолот {} од ({}, {})'.format(vertex_to_expand, current_path_weight, vertex_list))
        # На оваа линија код, сигурни сме дека не сме го разграниле моменталниот јазол. Го разгрануваме така што пребаруваме низ сите негови соседи.
        for neighbour, new_weight in graph.neighbours(vertex_to_expand):
            if neighbour in expanded:
                if verbose:
                    print('{} е веќе разгранет'.format(neighbour))
            else:
                # Ако моменталниот сосед не е разгранет, го додаваме во редицата на јазли за разгранување.
                if verbose:
                    print('{} со тежина {}, кој е соседен јазол на {}, го додаваме во редот за разгранување со нова '
                          'цена и го означуваме како разгранет'.format(neighbour, new_weight, vertex_to_expand))
                # Дојавата која ја користиме е функција добиена како аргумент бидејќи функцијата на дојава е различна за секој проблем.
                heuristic = heuristic_function(neighbour, goal_vertex)
                # Новата вредност на поминатата патека е досегашната патека + новата тежина
                path_weight = current_path_weight + new_weight
                # А тежината во А-ѕвезда е досегашната патека + новата тежина + тежината од дојавата.
                a_star_weight = path_weight + alpha * heuristic
                # Бидејќи ова е пребарување А-ѕвезда, соседот кој го додаваме ќе биде соодветно додаден преку библиотеката heapq.
                heapq.heappush(queue, ((a_star_weight, path_weight), vertex_list + [neighbour]))
        # Откако го разгранивме јазолот, го додаваме во множеството разгранети јазли.
        expanded.add(vertex_to_expand)
        if verbose:
            print()
