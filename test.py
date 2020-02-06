from flask import Flask,render_template,request,redirect,jsonify
from werkzeug import secure_filename
#import psycopg2
import copy
#import MySQLdb
import json
import mysql.connector
from collections import defaultdict
import pandas as pd
#import pandasql as ps
import warnings
import re
import datetime as dt
import os
from pandas.api.types import is_numeric_dtype
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import squarify 


warnings.filterwarnings('ignore')

app = Flask(__name__)

all_databaselists = {}
alldata = {}
dataframe_uni = {}


@app.route('/')
def hello_world():
   return render_template('MainFrame.html')


@app.route('/crm')
def next_page():
   return render_template('CRM.html')   

   
@app.route('/databaseconnections',methods = ['POST', 'GET'])
def db_connections():
    if request.method == 'POST':
        dbtype = 'MYSQL'
        dbuser = 'root'
        dbpw = '12345678'
        hname = '127.0.0.1'
        hport = '3306'
        dbname = 'test'
# =============================================================================
#         dbtype = request.form.get('dbtype')
#         dbuser = request.form.get('dbuser')
#         dbpw = request.form.get('dbpw')
#         hname = request.form.get('hname')
#         hport = request.form.get('hport')
#         dbname = request.form.get('dbname')
# =============================================================================
        if(dbtype == "MYSQL"):
            connection = mysql.connector.connect(user = dbuser,
                                  password = dbpw,
                                  host = hname,
                                  port = hport,
                                  database = dbname)
            cursor = connection.cursor(buffered=True)
            def get_table_col_names(table_str):
                all_databaselists = {}
                for i in table_str:
                    cursor.execute("select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS \
                                   where TABLE_NAME= '%s'" % (i))
                    tableDesc1 = cursor.fetchall()
                    print ('tableDesc1', tableDesc1)
                    tableDesc = [i[0] for i in tableDesc1]
                    print (tableDesc)
                    all_databaselists[i] = tableDesc
                    with open('static/data.json','w') as f:
                        json.dump(all_databaselists,f)
                return all_databaselists

        
                        
        cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_type = \
                       'BASE TABLE' AND table_schema='test'")
        candidate_records = cursor.fetchall() 
        print (candidate_records)
            #res = [''.join(i) for i in candidate_records]
        res = [i[0] for i in candidate_records]
            
        all_cols = get_table_col_names(res)
        print ('all colu',all_cols)
        

        alldata.update(all_cols)
        cursor.close()           
    
                
    return render_template('database_connections.html')


@app.route('/rfm_seg',methods = ['POST', 'GET'])

def rfm_segmentation():
    
    return  render_template('rfm_segmentation.html',data=alldata) 


@app.route('/tablevalues',methods = ['POST', 'GET'])
def tabledata():
    if request.method == 'POST':
    ##################### GET ALL THE TABLE SELECTED VALUES HERE ###########################################
    ################ ROW 1 OF TABLE VALUES ################################
        table1 = request.form.get('firsttablename');
        jointype1 = request.form.get('jointype1');
        table11 = request.form.get('21');
        column1 = request.form.get('coloft1');
        equal1 =  request.form.get('join1');
        column11 = request.form.get('colot21');
        print (table1,jointype1,table11)
        print ('select * from', table1, jointype1, table11, 'ON', table1,'.',column1, equal1 ,table11,'.',column11 )

    ################ ROW 2 OF TABLE VALUES ################################    
        table2 = request.form.get('firsttablename1');
        jointype2 = request.form.get('jointype2');
        table22 = request.form.get('221');
        columns2 = request.form.get('colo2');
        equal2 =  request.form.get('join2');
        columns22 = request.form.get('colot22');

    ################ ROW 3 OF TABLE VALUES ################################    
        table3 = request.form.get('firsttablename2');
        jointype3 = request.form.get('jointype3');
        table33 = request.form.get('231');
        columns3 = request.form.get('colo3');
        equal3 =  request.form.get('join3');
        columns33 = request.form.get('colot23');

    ################ ROW 4 OF TABLE VALUES ################################    
        table4 = request.form.get('firsttablename3');
        jointype4 = request.form.get('jointype4');
        table44 = request.form.get('241');
        columns4 = request.form.get('colo4');
        equal4 =  request.form.get('join4');
        columns44 = request.form.get('colot24');

    ################ ROW 5 OF TABLE VALUES ################################    
        table5 = request.form.get('firsttablename4');
        jointype5 = request.form.get('jointype5');
        table55 = request.form.get('251');
        columns5 = request.form.get('colo5');
        equal5 =  request.form.get('join5');
        columns55 = request.form.get('colot25');

    ################ ROW 2 OF 1 TABLE VALUES ################################  
        rfmtable1 = request.form.get('rfmtablename1');
        rfmtable2 = request.form.get('rfmtablename2');
        rfmtable3 = request.form.get('rfmtablename3');
        rfmtable4 = request.form.get('rfmtablename4');

        rfmtableoptions1 = request.form.get('rfmtableoptions1');
        rfmtableoptions2 = request.form.get('rfmtableoptions2');
        rfmtableoptions3 = request.form.get('rfmtableoptions3');
        rfmtableoptions4 = request.form.get('rfmtableoptions4');
        
        
        


        missval1 = request.form.get('miss_val1');
        missval2 = request.form.get('miss_val2');
        missval3 = request.form.get('miss_val3');
        missval4 = request.form.get('miss_val4');


    ################ FILTERS TABLE ################################   
        filtertable1 = request.form.get('selectname1');
        filtertable2 = request.form.get('selectname2');
        filtertable3 = request.form.get('selectname3');
        filtertable4 = request.form.get('selectname4');
        filtertable5 = request.form.get('selectname5');
        filtertable6 = request.form.get('selectname6');
        filtertable7 = request.form.get('selectname7');
        filtertable8 = request.form.get('selectname8');


        filtercolmap1 = request.form.get('selectname11');
        filtercolmap2 = request.form.get('selectname21');
        filtercolmap3 = request.form.get('selectname31');
        filtercolmap4 = request.form.get('selectname41');
        filtercolmap5 = request.form.get('selectname51');
        filtercolmap6 = request.form.get('selectname61');
        filtercolmap7 = request.form.get('selectname71');
        filtercolmap8 = request.form.get('selectname81');  

        filterjointype1 = request.form.get('selectname12');
        filterjointype2 = request.form.get('selectname22');
        filterjointype3 = request.form.get('selectname32');
        filterjointype4 = request.form.get('selectname42');
        filterjointype5 = request.form.get('selectname52');
        filterjointype6 = request.form.get('selectname62');
        filterjointype7 = request.form.get('selectname72');
        filterjointype8 = request.form.get('selectname82');

        filterinput1 = request.form.get('inputf1');
        filterinput2 = request.form.get('inputf2');
        filterinput3 = request.form.get('inputf3');
        filterinput4 = request.form.get('inputf4');
        filterinput5 = request.form.get('inputf5');
        filterinput6 = request.form.get('inputf6');
        filterinput7 = request.form.get('inputf7');
        filterinput8 = request.form.get('inputf8');

        def query_table():
            return [table1,jointype1,table11,column1,equal1,column11,
                    table2,jointype2,table22,columns2,equal2,columns22,
                    table3,jointype3,table33,
                    table4,jointype4,table44,
                    table5,jointype5,table55,
                    rfmtable2,rfmtable1,rfmtableoptions1,rfmtableoptions2,rfmtable3,
                    rfmtableoptions3,rfmtable4,rfmtableoptions4,
                    filtertable1,filtercolmap1,filterjointype1,filterinput1,
                    filtertable2,filtercolmap2,filterjointype2,filterinput2,
                    filtertable3,filtercolmap3,filterjointype3,filterinput3,
                    filtertable4,filtercolmap4,filterjointype4,filterinput4,
                    filtertable5,filtercolmap5,filterjointype5,filterinput5,
                    filtertable6,filtercolmap6,filterjointype6,filterinput6,
                    filtertable7,filtercolmap7,filterjointype7,filterinput7,
                    filtertable8,filtercolmap8,filterjointype8,filterinput8]
            
        query_data = query_table()
        str_list = [x for x in query_data if x != '']
        str_list_ = [x for x in str_list if x is not None]
        

        s1 =  (f"select {rfmtable1}.{rfmtableoptions1},{rfmtable2}.{rfmtableoptions2}, \
                   {rfmtable3}.{rfmtableoptions3},{rfmtable4}.{rfmtableoptions4} \
                   from {table1} {jointype1} {table11} ON \
                 {table1}.{column1} {equal1} {table11}.{column11} \
                 {jointype2} {table22} ON {table2}.{columns2}{equal2}{table22}.{columns22} \
                 {jointype3} {table3} ON {table3}.{columns3}{equal3}{table33}.{columns33} \
                 {jointype4} {table4} ON {table4}.{columns4}{equal4}{table44}.{columns44} \
                 {jointype5} {table5} ON {table5}.{columns5}{equal5}{table55}.{columns55}\
                 where \
                 {filtertable1}.{filtercolmap1} {filterjointype1} ({filterinput1}) \
                 and {filtertable2}.{filtercolmap2} {filterjointype2} ({filterinput2}) \
                 and {filtertable3}.{filtercolmap3} {filterjointype3} ({filterinput3}) \
                 and {filtertable4}.{filtercolmap4} {filterjointype4} ({filterinput4}) \
                 and {filtertable5}.{filtercolmap5} {filterjointype5} ({filterinput5}) \
                 and {filtertable6}.{filtercolmap6} {filterjointype6} ({filterinput6}) \
                 and {filtertable7}.{filtercolmap7} {filterjointype7} ({filterinput7}) \
                 and {filtertable8}.{filtercolmap8} {filterjointype8} ({filterinput8}) \
                 group by 1,2,3,4")
        
        
        s2 = s1.replace("and .  ()","").replace("ON .None","").replace("ON.None","").replace(".None","")
        
        s = re.sub(r'and \. \(\).*?(?=group)', '', s2, flags=re.S)
        print("query",s)
        with open('./templates/queries','a+') as f:
            f.write(s)
        dbtype = 'MYSQL'
        dbuser = 'root'
        dbpw = '12345678'
        hname = '127.0.0.1'
        hport = '3306'
        dbname = 'test'
        connection = mysql.connector.connect(user = dbuser,
                                  password = dbpw,
                                  host = hname,
                                  port = hport,
                                  database = dbname)

        cursor = connection.cursor()
        cursor.execute(s)
        a = cursor.fetchall()
        print ('a',a)
        df = pd.DataFrame(a, columns =['Customer','Recency', 'Frequency', 'Monetory']) 
        df.to_csv('./static/test.csv', index=False)
        print(str(df))
# =============================================================================
#         if df.empty == True:
#             print ('no data to show')
#         else:
#             return  render_template('data.html',query=df)
# =============================================================================
        with open('templates/test.html','w') as f:
             f.write(str(df))
        
        f_bins=15
        m_bins=15
        r_bins=15
        uid_impute='Delete the row'
        frequency_impute='mode'
        monetary_impute='mean'
        recency_impute='median'
        def imputation_type(df,col_name,type_imp):
            #zero mean mode delete the row median max min
            if type_imp=="Delete the Row":
                df=df.dropna(subset=[col_name])
            elif type_imp=="Mean":
                df[col_name]=df[col_name].fillna(df[col_name].mean())
            elif type_imp=='Mode':
                df[col_name]=df[col_name].fillna(df[col_name].mode())
            elif type_imp=='Median':
                df[col_name]=df[col_name].fillna(df[col_name].median())
            elif type_imp=='Zero':
                df[col_name]=df[col_name].fillna(0)
            elif type_imp=='Max':
                df[col_name]=df[col_name].fillna(df[col_name].max())
            elif type_imp=='Min':
                df[col_name]=df[col_name].fillna(df[col_name].min())
            return df
        master_data=pd.read_csv("./static/test.csv")
        def crm(master_data,f_bins,m_bins,r_bins,uid_impute,frequency_impute,monetary_impute,recency_impute):
            rules=pd.read_excel("./input/rules_rfm.xlsx")
            rules['concat_tag']=rules['Recency']+','+rules['Frequency']+','+rules['Monetary']
            rule_dict=rules.set_index('concat_tag').to_dict()
            #rule_dict['tag']
        
            ### Come up with a better practise
            master_data.columns=['unique_identifier','recency','frequency','monetary']
        
            if is_numeric_dtype(master_data.recency):
                pass
            else:
                master_data.recency=pd.to_datetime(master_data.recency)
                master_data['act_recency']=master_data.recency.apply(lambda x: ((datetime.now()-x).total_seconds())/(60*60*24)  )
                master_data.drop(['recency'],inplace=True, axis=1)
                master_data.rename(columns={'act_recency':'recency'},inplace=True)
        
        
        
            master_data.head()
        
            ##### Checking quantiles based on the bins
        
            plt.figure(figsize=(12,10))
            plt.subplot(3, 1, 1); 
            sns.distplot(master_data['recency'])
            plt.subplot(3, 1, 2); 
            sns.distplot(master_data['frequency'])
            plt.subplot(3, 1, 3); 
            sns.distplot(master_data['monetary'])
            #plt.show()
        
        
            ####### missing values logic here
        
            master_data=imputation_type(master_data,'recency',recency_impute)
            master_data=imputation_type(master_data,'frequency',frequency_impute)
            master_data=imputation_type(master_data,'monetary',monetary_impute)
            master_data=imputation_type(master_data,'unique_identifier',uid_impute)
        
            master_data=master_data.groupby(['unique_identifier']).agg({'recency':'min','frequency':'sum','monetary':'sum'}).reset_index()
        
            r_labels = range(r_bins+1, 1, -1); 
            f_labels = range(1, f_bins+1)
            m_labels = range(1, m_bins+1)
        
        
            r_groups = pd.qcut(master_data['recency'], q=r_bins,duplicates='drop')
            f_groups = pd.qcut(master_data['frequency'], q=f_bins,duplicates='drop')
            m_groups = pd.qcut(master_data['monetary'], q=m_bins,duplicates='drop')#, labels=m_labels)
        
            master_data = master_data.assign(R = r_groups.values, F = f_groups.values, M=m_groups.values)
            master_data.head()
        
        
            f_val=master_data.F.value_counts().reset_index().sort_values('index').reset_index()
            f_val.rename(columns={'level_0':'score','index':'bin'},inplace=True)
            f_val['score']=f_val['score']+1
            f_val.set_index('bin',inplace=True)
            f_label=f_val.to_dict()
        
            r_val=master_data.R.value_counts().reset_index().sort_values('index').reset_index()
            r_val.rename(columns={'level_0':'score','index':'bin'},inplace=True)
            r_val['score']=r_val['score']+1
            r_val.set_index('bin',inplace=True)
            r_label=r_val.to_dict()
        
            m_val=master_data.M.value_counts().reset_index().sort_values('index').reset_index()
            m_val.rename(columns={'level_0':'score','index':'bin'},inplace=True)
            m_val['score']=m_val['score']+1
            m_val.set_index('bin',inplace=True)
            m_label=m_val.to_dict()
        
            master_data['r_score']=master_data.R.apply(lambda x : r_label['score'][x])
            master_data['f_score']=master_data.F.apply(lambda x : f_label['score'][x])
            master_data['m_score']=master_data.M.apply(lambda x : m_label['score'][x])
        
            ###### Heatmap vizualization
        
        
            master_data.sort_values(['m_score'],inplace=True)
            rm_map= master_data.pivot_table(index="r_score", columns="m_score",values='unique_identifier',aggfunc='count')
            rm_map.sort_index(ascending=False,inplace=True)
            rm_map.fillna(0,inplace=True)
            arr = rm_map.values
            vmin, vmax = arr.min(), arr.max()
            plt.subplots(figsize=(20,15))
        
            ax=sns.heatmap(rm_map, annot=True, fmt="f", vmin=vmin, vmax=vmax,linewidths=.5,cmap="GnBu")
            ax.set_title("Score Distribution - RM", fontsize=18)
            ax.set_xlabel("Monetary Score", fontsize=12
                         );
            ax.set_ylabel("Recency Score", fontsize=12
                         );
            plt.savefig("./static/plots/rm_map.png")
            #plt.show()
        
        
            master_data.sort_values(['m_score'],inplace=True)
        
            fm_map= master_data.pivot_table(index="f_score", columns="m_score",values='unique_identifier',aggfunc='count')
            fm_map.sort_index(ascending=False,inplace=True)
            fm_map.fillna(0,inplace=True)
        
            arr = fm_map.values
        
            vmin, vmax = arr.min(), arr.max()
            plt.subplots(figsize=(20,15))
        
            ax=sns.heatmap(fm_map, annot=True, fmt="f", vmin=vmin, vmax=vmax,linewidths=.5,cmap="GnBu")
            ax.set_title("Score Distribution - FM", fontsize=18)
            ax.set_xlabel("Monetary Score", fontsize=12
                         );
            ax.set_ylabel("Frequency Score", fontsize=12
                         );
            plt.savefig("./static/plots/fm_map.png")
        
            #plt.show()
        
            master_data.sort_values(['f_score'],inplace=True)
        
            rf_map= master_data.pivot_table(index="r_score", columns="f_score",values='unique_identifier',aggfunc='count')
            rf_map.fillna(0,inplace=True)
            rf_map.sort_index(ascending=False,inplace=True)
        
            arr = rf_map.values
            vmin, vmax = arr.min(), arr.max()
            plt.subplots(figsize=(20,15))
        
            ax=sns.heatmap(rf_map, annot=True, fmt="f", vmin=vmin, vmax=vmax,linewidths=.5,cmap="GnBu")
            ax.set_title("Score Distribution - RF", fontsize=18)
            ax.set_xlabel("Frequency Score", fontsize=12
                         );
            ax.set_ylabel("Recency Score", fontsize=12
                         );
            plt.savefig("./static/plots/rf_map.png")
        
            #plt.show()
        
        
            master_data['r_score']=master_data['r_score'].astype(int)
            master_data['m_score']=master_data['m_score'].astype(int)
            master_data['f_score']=master_data['f_score'].astype(int)
        
            ###### 33rd percentile of the rank
            # quantiles = master_data[['r_score','m_score','f_score']].quantile(q=[0.33]).to_dict()
        
            r_thresh_1=round(master_data['r_score'].max() *0.33)
            m_thresh_1=round(master_data['f_score'].max() *0.33)
            f_thresh_1=round(master_data['m_score'].max() *0.33)
        
            r_thresh_2=round(master_data['r_score'].max() *0.66)
            m_thresh_2=round(master_data['f_score'].max() *0.66)
            f_thresh_2=round(master_data['m_score'].max() *0.66)
        
            r_thresh_1,f_thresh_1,m_thresh_1
        
            r_thresh_2,f_thresh_2,m_thresh_2
        
            master_data['r_tag']=master_data.r_score.apply(lambda x : 'High' if x> r_thresh_2 else 'Medium' if x>r_thresh_1 else 'Low')
            master_data['f_tag']=master_data.f_score.apply(lambda x : 'High' if x> f_thresh_2 else 'Medium' if x>f_thresh_1 else 'Low')
            master_data['m_tag']=master_data.m_score.apply(lambda x : 'High' if x> m_thresh_2 else 'Medium' if x>m_thresh_1 else 'Low')
        
            master_data['r_tag'].value_counts()
        
            master_data['m_tag'].value_counts()
        
            master_data['f_tag'].value_counts()
        
            master_data['concat_tag']=master_data['r_tag']+','+master_data['f_tag']+','+master_data['m_tag']
            master_data['Segment']=master_data['concat_tag'].apply(lambda x : rule_dict['tag'][x])
        
            master_data['concat_tag'].unique()
        
            df_viz = master_data.groupby('Segment').size().reset_index(name='counts')
            df_viz
        
            labels = df_viz.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
            sizes = df_viz['counts'].values.tolist()
            colors = [plt.cm.Set3(i/float(len(labels))) for i in range(len(labels))]
        
            # Draw Plot
            plt.figure(figsize=(12,8), dpi= 80)
            ax=squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)
            ax.set_title("Segment wise Distribution", fontsize=18)

            strFile  = './static/plots/segment_distribution.png'

            if os.path.isfile(strFile): 
                os.remove(strFile) 
                plt.savefig('./static/plots/segment_distribution.png')
        
            #plt.show()
        
            unique_segments=list(master_data.Segment.unique())
        
            for i in unique_segments:
                temp=master_data[master_data.Segment==i]
                master_data.loc[master_data.Segment==i,"Median Frequency "]=temp.frequency.median()
                master_data.loc[master_data.Segment==i,"Median Monetary "]=temp.monetary.median()
                master_data.loc[master_data.Segment==i,"Median Recency "]=temp.recency.median()
        
        
        
            master_data_mini=master_data[["Segment","Median Monetary ","Median Frequency ","Median Recency "]].drop_duplicates()
        
        
            temp=master_data_mini[["Segment","Median Monetary "]]
            temp.set_index("Segment",inplace=True)
            ax=temp.plot.barh()
            for val in ax.patches:
                ax.text(val.get_width()+.1, val.get_y()+.4, \
                    str(round((val.get_width()), 2)), fontsize=8, color='black')
        
            ax.set_alpha(0.8)
            ax.set_title("Segment wise - Median Monetary", fontsize=18)
            ax.set_xlabel("Median Monetary", fontsize=12
                         );
            ax.set_ylabel("Segments", fontsize=12
                         );
            ax.invert_yaxis()
            ax.get_legend().remove()
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
        
            plt.savefig("./static/plots/Segment_wise-Median_Monetary.png")
        
            #plt.show()
        
        
            temp=master_data_mini[["Segment","Median Recency "]].drop_duplicates()
            temp.set_index("Segment",inplace=True)
            ax=temp.plot.barh()
            for val in ax.patches:
                ax.text(val.get_width()+.1, val.get_y()+.4, \
                    str(round((val.get_width()), 2)), fontsize=8, color='black')
        
            ax.set_alpha(0.8)
            ax.set_title("Segment wise - Median Recency", fontsize=18)
            ax.set_xlabel("Median Recency", fontsize=12
                         );
            ax.set_ylabel("Segments", fontsize=12
                         );
            ax.invert_yaxis()
            ax.get_legend().remove()
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            plt.savefig("./static/plots/Segment_wise-Median_Recency.png")
        
        
            #plt.show()
        
            temp=master_data_mini[["Segment","Median Frequency "]].drop_duplicates()
            temp.set_index("Segment",inplace=True)
            ax=temp.plot.barh()
            for val in ax.patches:
                ax.text(val.get_width()+.1, val.get_y()+.4, \
                    str(round((val.get_width()), 2)), fontsize=8, color='black')
        
        
            ax.set_alpha(0.8)
            ax.set_title("Segment wise - Median Frequency", fontsize=18)
            ax.set_xlabel("Median Frequency", fontsize=12
                         );
            ax.set_ylabel("Segments", fontsize=12
                         );
            ax.invert_yaxis()
            ax.get_legend().remove()
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            plt.savefig("./static/plots/Segment_wise-Median_Frequency.png")
        
            #plt.show()
        
        
            rf_map= master_data.pivot_table(index="r_score", columns="f_score",values='monetary',aggfunc='median')
            rf_map.sort_index(ascending=False,inplace=True)
        
            arr = rf_map.values
            vmin, vmax = arr.min(), arr.max()
            plt.subplots(figsize=(20,15))
        
            ax=sns.heatmap(rf_map, annot=True, fmt="f", vmin=vmin, vmax=vmax,linewidths=.5,cmap="GnBu")
            ax.set_title("Score Distribution - RF", fontsize=18)
            ax.set_xlabel("Frequency Score", fontsize=12
                          );
            ax.set_ylabel("Recency Score", fontsize=12
                          );
            plt.savefig("./static/plots/rf_map_median.png")
        
            #plt.show()
        
        
        
            fm_map= master_data.pivot_table(index="f_score", columns="m_score",values='recency',aggfunc='median')
            fm_map.sort_index(ascending=False,inplace=True)
        
            arr = fm_map.values
            vmin, vmax = arr.min(), arr.max()
            plt.subplots(figsize=(20,15))
        
            ax=sns.heatmap(fm_map, annot=True, fmt="f", vmin=vmin, vmax=vmax,linewidths=.5,cmap="GnBu")
            ax.set_title("Score Distribution - FM", fontsize=18)
            ax.set_xlabel("Frequency Score", fontsize=12
                          );
            ax.set_ylabel("Monetary Score", fontsize=12
                          );
            plt.savefig("./static/plots/fm_map_median.png")
        
            #plt.show()
        
        
        
            rm_map= master_data.pivot_table(index="r_score", columns="m_score",values='frequency',aggfunc='median')
            rm_map.sort_index(ascending=False,inplace=True)
        
            arr = rm_map.values
            vmin, vmax = arr.min(), arr.max()
            plt.subplots(figsize=(20,15))
        
            ax=sns.heatmap(rm_map, annot=True, fmt="f", vmin=vmin, vmax=vmax,linewidths=.5,cmap="GnBu")
            ax.set_title("Score Distribution - FM", fontsize=18)
            ax.set_xlabel("Recency Score", fontsize=12
                          );
            ax.set_ylabel("Monetary Score", fontsize=12
                          );
            plt.savefig("./static/plots/rm_map_median.png")
        
            #plt.show()
        
        
            final_master_data=master_data[['unique_identifier', 'frequency', 'monetary', 'recency', 'Segment', 'Median Frequency ', 'Median Monetary ',
                   'Median Recency ']]
            
            return final_master_data,master_data_mini
        a,b=crm(master_data,f_bins,m_bins,r_bins,uid_impute,frequency_impute,monetary_impute,recency_impute)
       
        htmlpart = b.to_html();
     
        a.to_csv('data.csv');
        print("FILLED DATA",dataframe_uni)
        b.to_csv('rfm.csv')

        with open('templates/htmlpart.html','w+') as f:
            f.write(htmlpart)

    return render_template('htmlpart.html')

@app.route('/reports',methods = ['POST', 'GET'])
def allreports():
    return  render_template('reports.html')     


@app.route('/display_reports',methods = ['POST', 'GET'])
def displayallreports():


    #df = pd.read_csv('data.csv');
    #dataframe_uni = df.to_dict();
    df = pd.DataFrame()
    # dataframe_uni = df.to_dict();
    reports = request.args.get('deptname');
    reports = request.args.get('deptname');
    reports = request.args.get('deptname');
    reports = request.args.get('deptname');

    print(reports)
    if(reports == "singledata"):
        df = pd.read_csv('data.csv')
        print (df)
    elif(reports == "tabdata"):
        df = pd.read_csv('rfm.csv')
        print (df)

    return  render_template('display_reports.html',data=reports,dataframe_display=df);    
    

if __name__ == '__main__':
   app.debug = True
   app.run(host='0.0.0.0')
