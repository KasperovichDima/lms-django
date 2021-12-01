def qset_to_html(qset):
    if len(qset) == 0:
        return 'Empty recordset'
    return '<br>'.join(str(_) for _ in qset)
