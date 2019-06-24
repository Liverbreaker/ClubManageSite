import sys, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MYPATH = os.path.join(BASE_DIR, 'out.txt')

def p2f(data, file='out.txt'):
    fp = open(file, 'w') # 'a' for append
    fp.write(str(data))
    fp.close()

def get_model_field_names(model, ignore_fields=['content_object']):
    '''
    ::param model is a Django model class
    ::param ignore_fields is a list of field names to ignore by default
    This method gets all model field names (as strings) and returns a list
    of them ignoring the ones we know don't work (like the 'content_object' field)
    '''
    model_fields = model._meta.get_fields()
    model_field_names = list(set([f.name for f in model_fields if f.name not in ignore_fields]))
    return model_field_names
    
def get_lookup_fields(model, fields=None):
    '''
    ::param model is a Django model class
    ::param fields is a list of field name strings.
    This method compares the lookups we want vs the lookups
    that are available. It ignores the unavailable fields we passed.
    '''
    model_field_names = get_model_field_names(model)
    if fields is not None:
        '''
        we'll iterate through all the passed field_names
        and verify they are valid by only including the valid ones
        '''
        lookup_fields = []
        for x in fields:
            if "__" in x:
                # the __ is for ForeignKey lookups
                lookup_fields.append(x)
            elif x in model_field_names:
                lookup_fields.append(x)
    else:
        '''
        No field names were passed, use the default model fields
        '''
        lookup_fields = model_field_names
    return lookup_fields


def qs_to_dataset(qs, fields=None):
    '''
    ::param qs is any Django queryset
    ::param fields is a list of field name strings, ignoring non-model field names
    This method is the final step, simply calling the fields we formed on the queryset
    and turning it into a list of dictionaries with key/value pairs.
    '''

    lookup_fields = get_lookup_fields(qs.model, fields=fields)
    return list(qs.values(*lookup_fields))

def qs_to_local_csv(qs, fields=None, path=None, filename=None):
    if path is None:
        path = os.path.join(os.path.dirname(BASE_DIR), 'csvstorage')
        if not os.path.exists(path):
            '''
            CSV storage folder doesn't exist, make it!
            '''
            os.mkdir(path)
    if filename is None:
        model_name = slugify(qs.model.__name__)
        filename = "{}.csv".format(model_name)
    filepath = os.path.join(path, filename)
    lookups = get_lookup_fields(qs.model, fields=fields)
    dataset = qs_to_dataset(qs, fields)
    rows_done = 0
    with open(filepath, 'w') as my_file:
        writer = csv.DictWriter(my_file, fieldnames=lookups)
        writer.writeheader()
        for data_item in dataset:
            writer.writerow(data_item)
            rows_done += 1
    print("{} rows completed".format(rows_done))
