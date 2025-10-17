import pandas as pd
from . import config
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import Patch

import logging

logging.getLogger('matplotlib').setLevel(logging.WARNING)
logging.getLogger('PIL').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


def norm(s : str) -> str:
    if not isinstance(s, str):
        return ''
    
    if ':' in s:
        return s.split(':')[0].lower().strip()
    
    return s.lower().strip()

def stat_to_pdf(statistik_summary : dict, semestrs_dfs : dict):
    
    def sports_bars(pdf : PdfPages):
        
        sports = statistik_summary['sports_satisfaction']
        
        x_axis = list(sports.index)
        y_axis = list(sports['mean_satisfaction'])
        
        plt.figure(figsize=(10, 6))  # Размер графика, чтобы надписи не налезали
        
        max_y = max(y_axis) if y_axis else 1
        if max_y == 0:
            max_y = 1
        
        norm = [y / max_y for y in y_axis]   
        colors = [plt.cm.Blues(val) for val in norm]
        
        bars = plt.bar(x_axis, y_axis, width= 0.6, color = colors)
        
        font_title = {'family' : 'serif', 'color' : '#4F81BD', 'size' : 20}
        font_label = {'family' : 'serif', 'color' : 'red', 'size' : 15}
        
        plt.title('Sports mean satisfaction', fontdict= font_title)
        plt.xlabel('Sport', fontdict= font_label)
        plt.ylabel('Satisfaction', fontdict= font_label)
        
        plt.grid(axis='y', linestyle = '--', color = 'red', linewidth = 1)
        
        plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{int(y)}%'))
        
        plt.gca().set_facecolor("#f9f9f9")
        
        plt.ylim(0, max(y_axis) + 5)
        
        for i, bar in enumerate(bars):
            
            bar_width = bar.get_width()
            bar_x = bar.get_x()
            bar_height = bar.get_height()
            
            plt.text(x = bar_x + bar_width / 2, y = bar_height, s = f"{bar_height}%", ha='center', va='bottom')
        
        plt.tight_layout()
        pdf.savefig()
        plt.close()
        
    def semestr_bars(pdf : PdfPages):
        
        semestrs_satisfaction = statistik_summary['semestrs_satisfaction']
        
        x_axis = [0,1,2]
        y_axis = list(semestrs_satisfaction['mean_satisfaction'])

        plt.figure(figsize=(10, 6))  # Размер графика, чтобы надписи не налезали
        
        max_y = max(y_axis) if y_axis else 1
        if max_y == 0:
            max_y = 1
        
        norm = [y / max_y for y in y_axis]   
        colors = [plt.cm.Blues(val) for val in norm]
        
        bars = plt.bar(x_axis, y_axis, width= 0.6, color = colors)
        
        font_title = {'family' : 'serif', 'color' : '#4F81BD', 'size' : 20}
        font_label = {'family' : 'serif', 'color' : 'red', 'size' : 15}
        
        plt.title('Semestrs mean satisfaction', fontdict= font_title)
        plt.xlabel('Semestr', fontdict= font_label)
        plt.ylabel('Satisfaction', fontdict= font_label)
        
        plt.grid(axis='y', linestyle = '--', color = 'red', linewidth = 1)
        
        plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{int(y)}%'))
        plt.gca().xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{list(semestrs_satisfaction.index)[int(x)] if int(x) < len(semestrs_satisfaction.index) else ""}'))
        
        plt.xticks(x_axis)
        
        plt.gca().set_facecolor("#f9f9f9")
        
        plt.ylim(0, max(y_axis) + 5)
        
        for i, bar in enumerate(bars):
            
            bar_width = bar.get_width()
            bar_x = bar.get_x()
            bar_height = bar.get_height()
            
            plt.text(x = bar_x + bar_width / 2, y = bar_height, s = f"{bar_height}%", ha='center', va='bottom')
        
        plt.tight_layout()
        pdf.savefig()
        plt.close()
        
    def distribution_pie(pdf : PdfPages):
        
        dist = statistik_summary['satisfaction_distribution']
        
        sizes = list(dist.values)
        labels = list(dist.index)
        colors = config.PIE_COLORS
        
        filtered_sizes = [size for size in sizes if size > 0]
        filtered_labels = [label for label, size in zip(labels, sizes) if size > 0]
        filtered_colors = [color for color, size in zip(colors, sizes) if size > 0]
        
        
        plt.figure(figsize= (10, 6))
        
        plt.pie(x= filtered_sizes, labels= filtered_labels, colors= filtered_colors)
        
        handles = [Patch(facecolor=c, label=l) for c, l in zip(colors, labels)]
        plt.legend(handles = handles,title = 'Distribution', loc = 'upper right')
        
        plt.suptitle(t= 'Satisfaction distribution Pie-Chart', fontsize=16, color="#4F81BD")
        
        plt.tight_layout()
        pdf.savefig()
        plt.close()
    
    def satisfaction_table(pdf : PdfPages):
        
        def max_cols_width(tabl):
            
            max_width = 0
            
            for key, cell in tabl.get_celld().items():

                text = cell.get_text().get_text()
                width = len(text) * 0.01
                
                if max_width < width:
                    max_width = width
            
            max_width = min(max_width, 0.3)
            
            for key, cell in tabl.get_celld().items():
                cell.set_width(max_width)
        
        personal_sat = statistik_summary['personal']
        
        distribution = config.SATISFACTION_DISTRIBUTION
        colors = config.TABLE_COLORS
        
        ranges = [[float(frm), float(to)] for frm, to in (d.replace('%', '').split('-') for d in distribution)]
        
        for semestr in config.SEMESTRS:
            
            df = semestrs_dfs[semestr]
            cur_semestr = f"{semestr}_satisfaction"
            
            
            fig, ax = plt.subplots(figsize = (10, 4 + len(df.values) * 0.2))
            ax.axis('off')
            
            plt.suptitle(f"{semestr}")
            
            tabl = ax.table(cellText= df.values, colLabels= df.columns, cellLoc= 'center', loc= 'center', colWidths=[0.18]*len(df.columns))
            tabl.scale(1.3, 1.3)
            tabl.auto_set_font_size(False)
            tabl.set_fontsize(12)
            
            for row in range(1, len(df) + 1):
                
                for col in range(len(df.columns)):
                    
                    cell = tabl[(row, col)]
                    student = norm(cell.get_text().get_text())
                    
                    cell.set_edgecolor("#cccccc")
                    
                    if not student or student == 'nan':
                        cell.get_text().set_text('')
                        continue
                    
                    match = personal_sat.loc[personal_sat['student'] == student, cur_semestr]
                    if not match.empty:
                        satisfaction = match.values[0]
                    else:
                        logger.warning(f"no student like {student} found!")
                    
                    for i, ran in enumerate(ranges):
                        
                        if ran[0] <= satisfaction <= ran[1]:
                            cell.set_facecolor(colors[i])
            
            handles = [Patch(facecolor=c, label=l) for c, l in zip(colors, distribution)]
            plt.legend(handles = handles,title = 'Distribution Range', loc = 'upper right', bbox_to_anchor=(1.05, 1))
            
            max_cols_width(tabl)
            
            plt.tight_layout()
            pdf.savefig()
            plt.close()
    
    def stat_metriks_table(pdf : PdfPages):
        
        metriks = statistik_summary['solo_stat']
        
        logger.info(metriks)
        
        fig, ax = plt.subplots(figsize = (10, 4))
        
        ax.axis('off')
        
        met_df = pd.DataFrame.from_dict(data= metriks, orient= 'index', columns= ['stat']).reset_index(names= 'metrik')
        
        logger.info(met_df)
        
        tabl = plt.table(cellText= met_df.values, colLabels= met_df.columns, cellLoc= 'center', loc= 'center', colWidths=[0.18]*len(met_df.columns))
        tabl.scale(1.3, 1.3)
        tabl.auto_set_font_size(False)
        tabl.set_fontsize(12)
        
        plt.title("General Statistics", fontsize=16, color="#4F81BD", pad=20)
        
        for (row, col), cell in tabl.get_celld().items():
            if row == 0:
                cell.set_facecolor("#4F81BD")
                cell.set_text_props(color="white", weight="bold")
            elif row % 2 == 0:
                cell.set_facecolor("#f2f2f2")
        
        plt.tight_layout()
        pdf.savefig()
        plt.close()
    
        
    with PdfPages(r'Output\statistik.pdf') as pdf:
        
        sports_bars(pdf)

        distribution_pie(pdf)

        semestr_bars(pdf)
    
        satisfaction_table(pdf)
        
        stat_metriks_table(pdf)

        plt.close('all')
    
    