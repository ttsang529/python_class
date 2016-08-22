import pandas

def csv_select_column(columns,save_file):
    colnames = ['sid','longitude','latitude','name','address','tel','wifi','notes']
    data = pandas.read_csv('stores_old.csv', names=colnames,encoding="Big5")
    df = pandas.DataFrame( data,columns=columns)
    df.to_csv(save_file)

if __name__ == '__main__':
    columns=['sid','name', 'address', 'wifi']
    save_file='stores_new.csv'
    csv_select_column(columns,save_file)


