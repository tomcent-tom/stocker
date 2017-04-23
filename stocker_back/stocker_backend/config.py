def convert_html_to_matrix(html):
    start_table = html.find('<table class="dataOverview"')
    end_table = html.find('</table>', start_table)
    j_table = []
    j_table.append(['Datum openbaarmaking', 'Href', 'Naam meldplichtige', 'Emittent'])
    index = start_table
    index = html.find('<tr>', index)+3
    while True:
        next_row = html.find('<tr>', index)
        index = next_row
        if next_row == -1 or next_row > end_table:
            break
        next_row_end = html.find('</tr>', index)
        row = []
        while True:
            next_cell = html.find('<td', index)
            if next_cell == -1 or next_cell > next_row_end:
                break
            index = next_cell
            next_cell_end = html.find('</td>',index)
            while True:
                index = html.find('>',index)+1
                if html[index] != '<':
                    href = html.find('href=', next_cell)
                    if href < next_cell_end:
                        href_end = html.find('">', href)
                        href = html[href + 6:href_end]
                        row.append(href)
                        href = next_cell_end
                    next_tab = html.find('<',index)
                    row.append(html[index:next_tab])
                    index = next_cell_end
                    break
        j_table.append(row)
    return j_table

def convert_matrix_to_table(matrix):
    json_data = []
    header = matrix[0]
    i = 0
    for row in matrix:
        if i != 0:
            json_row = {}
            j = 0
            for el in row:
                json_row[header[j]]=el
                j += 1
            json_data.append(json_row)
        i +=1
    return json_data

def get_extra_exco_data(html):
    start_table = html.find('<table class="dataOverview"')
    end_table = html.find('</table>', start_table)
    j_table = {}
    index = start_table
    index = html.find('<tr>', index)
    while True:
        next_row = html.find('<th', index)
        if next_row == -1 or next_row > end_table:
            break
        index = next_row
        next_cell_end = html.find('</th>', index)
        while True:
            index = html.find('>', index) + 1
            if html[index] != '<':
                next_tab = html.find('<', index)
                key = html[index:next_tab]
                index = next_cell_end
                break
        next_row = html.find('<td', index)
        if next_row == -1 or next_row > end_table:
            break
        index = next_row
        next_cell_end = html.find('</td>', index)
        while True:
            index = html.find('>', index) + 1
            if html[index] != '<':
                next_tab = html.find('<', index)
                j_table[key] = html[index:next_tab]
                index = next_cell_end
                break
    return j_table

Bel20 = {
    'ABI':
        {
            'ref':'ABI%3ABB',
            'exchange':'BB'
        },
    'ACKB':
        {
            'ref':'ACKB%3ABB',
            'exchange':'BB'
        },
    'AGS':
        {
            'ref':'AGS%3ABB',
            'exchange':'BB'
        },
    'APAM':
        {
            'ref':'APAM%3ANA',
            'exchange':'NA'
        },
    'BEKB':
        {
            'ref':'BEKB%3ABB',
            'exchange':'BB'
        },
    'BPOST':
        {
            'ref':'BPOST%3ABB',
            'exchange':'BB'
        },
    'COFB':
        {
            'ref':'COFB%3ABB',
            'exchange':'BB'
        },
    'COLR':
        {
            'ref':'COLR%3ABB',
            'exchange':'BB'
        },
    'ENGI':
        {
            'ref':'ENGI%3ABB',
            'exchange': 'BB'
        },
    'GLPG':
        {
            'ref':'GLPG%3ABB',
            'exchange': 'BB'
        },
    'GBLB':
        {
            'ref':'GBLB%3ABB',
            'exchange': 'BB'
        },
    'INGA':
        {
            'ref':'INGA%3ANA',
            'exchange': 'NA'
        },
    'KBC':
        {
            'ref':'KBC%3ABB',
            'exchange': 'BB'
        },
    'ONTEX':
        {
            'ref':'ONTEX%3ABB',
            'exchange': 'BB'
        },
    'PROX':
        {
            'ref':'PROX%3ABB',
            'exchange': 'BB'
        },
    'SOF':
        {
            'ref':'SOF%3ABB',
            'exchange': 'BB'
        },
    'SOLB':
        {
            'ref':'SOLB%3ABB',
            'exchange': 'BB'
        },
    'TNET':
        {
            'ref':'TNET%3ABB',
            'exchange': 'BB'
        },
    'UCB':
        {
            'ref':'UCB%3ABB',
            'exchange': 'BB'
        },
    'UMI':
        {
            'ref':'UMI%3ABB',
            'exchange': 'BB'
        },
}

Bloomber_url = 'https://www.bloomberg.com/markets/api/security/basic/'
fsma_url = {
    'baseline_search': 'http://www.fsma.be/nl/Supervision/fm/ma/trans_bl/TransactionsSearch.aspx?',
    'baseline_default': 'http://www.fsma.be/nl/Supervision/fm/ma/trans_bl/InsTrans.aspx',
    'other': 's=1&c=',
    'baseline_extra':'http://www.fsma.be'
}