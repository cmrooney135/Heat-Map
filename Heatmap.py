import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from matplotlib.colors import LinearSegmentedColormap

Top1 = ['A2', 'C2', 'A4', 'C4', 'A6', 'C6', 'A8', 'C8', 'A13', 'C13', 'A15', 'C15', 'A17', 'C17', 
       'A19', 'C19', 'A24', 'C24', 'A26', 'C26', 'A28', 'C28']
Top2 = ['A30', 'C30', 'A35', 'C35', 'A37', 'C37', 'A39', 'C39', 'A41', 'C41', 'A44', 'B44', 'C47', 
        'A47', 'C49', 'A49', 'C51', 'A51', 'C53', 'A53', 'C58', 'A58']
Top3 = ['C60', 'A60', 'C62','A62', 'C64', 'A64', 'C69', 'A69', 'C71',
        'A71', 'C73', 'A73', 'C75', 'A75', 'C80', 'A80', 'C82', 'A82', 'C84', 'A84', 'C86', 'A86']

Bottom1= ['G2', 'E2', 'G4', 'E4', 'G6', 'E6', 'G8', 'E8', 'G13', 'E13', 'G15', 'E15',
          'G17', 'E17', 'G19', 'E19', 'G24', 'E24', 'G26', 'E26', 'G28', 'E28']
Bottom2 = ['G30','E30','G35','E35','G37','E37','G39','E39','G41','E41',
            'F44','G44','E47','G47','E49','G49','E51','G51','E53','G53','E58','G58']
Bottom3 = ['E60','G60','E62','G62','E64','G64','E69','G69','E71','G71',
           'E73','G73','E75','G75','E80','G80','E82','G82','E84','G84','E86','G86']
Top = Top1 + Top2 + Top3
Bottom = Bottom1 + Bottom2 + Bottom3 


colors = [
    (0, 0, 1),       # deep blue
    (0.3, 0.3, 1),   # intermediate blue
    (0.6, 0.6, 1),   # light blue
    (1, 1, 1),       # white
    (1, 0.6, 0.6),   # light red
    (1, 0.3, 0.3),   # intermediate red
    (1, 0, 0)        # full red
]



nodes = [0.0, 1.0/6.0, 2.0/6.0, 3.0/6.0, 4.0/6.0, 5.0/6.0, 1.0]
custom_cmap = LinearSegmentedColormap.from_list("custom_red_extended", list(zip(nodes, colors)))

def display_matrix(cable):
    matrix = np.array(cable.matrix, dtype=np.float64)
    print(matrix)
    matrix1 = matrix[0].reshape(1, -1)  
    matrix2 = matrix[1].reshape(1, -1)
    sn = cable.serial_number

    fig, axes = plt.subplots(3, 1, figsize=(24, 8), 
                             gridspec_kw={'height_ratios': [1, 0.1, 1]})
    fig.suptitle(f'Heatmap for cable with SN: {sn}', fontsize=20)

    # Plot first heatmap with color bar
    
# Plot first heatmap
    sns.heatmap(matrix1, ax=axes[0], cmap=custom_cmap, annot=False, square=False,
                xticklabels=Top, yticklabels=[''], cbar=True, cbar_kws={'label': 'Intensity'},
                vmin=0.0, vmax=6.0)

    # Leave middle subplot blank
    axes[1].axis('off')

    # Plot second heatmap
    sns.heatmap(matrix2, ax=axes[2], cmap=custom_cmap, annot=False, square=False,
                xticklabels=Bottom, yticklabels=[''], cbar=True, cbar_kws={'label': 'Intensity'},
                vmin=0.0, vmax=6.0)


    # Adjust layout to make room for the title
    plt.tight_layout(rect=[0, 0, 1, 0.90])
    st.pyplot(plt)