def fixFilter(params, filter):
    q={}
    for f in filter:
      if type(filter[f]) is list:
        for i in range(len(filter[f])):
          q['filter[{}][{}][{}]'.format(f, i, 'key')] = filter[f][i]['key']
          q['filter[{}][{}][{}]'.format(f, i, 'value')] = filter[f][i]['value']
      else:
          q['filter[{}]'.format(f, 'value')] = filter[f]
  
    params.pop('filter', None)
    params.update(q)

    return params