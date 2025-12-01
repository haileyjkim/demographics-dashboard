import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io
import base64

# --- 1. Your Specific Function ---
def butterflyplot(X, title=None, colors=['crimson','royalblue']):
    L, R = X.columns.tolist()

    # Define figure parameters
    fig = plt.figure(figsize=(10, len(X)/2 + 1))
    
    # Create an axes to draw on
    ax = plt.subplot()
    
    # Plot the bars, flipping the left with negation
    ax.barh(y=X.index, width=-X[L], alpha=.75, color=colors[0], label=L)
    ax.barh(y=X.index, width=+X[R], alpha=.75, color=colors[1], label=R)
    
    # Create individual bar text labels
    text_props = {'c': 'black', 'va': 'center'}
    for y in X.index:
        x1 = X.loc[y, L]
        x2 = X.loc[y, R]
        # Safety check for rounding (handles non-integers gracefully)
        x1_label = str(round(x1)) if pd.notnull(x1) else "0"
        x2_label = str(round(x2)) if pd.notnull(x2) else "0"
        
        ax.text(-x1, y, x1_label, **text_props, ha='right')
        ax.text(+x2, y, x2_label, **text_props, ha='left')
    
    plt.legend(frameon=False)
    
    # Reduce ink
    sns.despine(left=True, bottom=True)
    ax.set_xticks([])
    ax.grid(axis='y', color='#F0F0F0', ls='--')

    if title:
        plt.title(title)

    return ax

# --- 2. The Flask Wrapper ---
def create_butterfly_plot(df):
    """
    Prepares the data and calls butterflyplot(), then returns base64 image.
    """
    try:
        # We need a DataFrame 'X' with exactly 2 numeric columns.
        
        X = df.copy()
        
        numeric_cols = X.select_dtypes(include=['number']).columns
        categorical_cols = X.select_dtypes(include=['object', 'category']).columns

        if len(categorical_cols) == 1 and len(numeric_cols) >= 1:
            X = pd.crosstab(X[numeric_cols[0]], X[categorical_cols[0]])
            
        elif len(X.columns) == 3:
             X = X.set_index(X.columns[0])
             
        # Ensure we strictly have 2 columns for Left and Right sides
        if len(X.columns) != 2:
            raise ValueError(f"Data formatting error: Plot requires exactly 2 groups (columns), found {len(X.columns)}.")
            
        # Call your function
        butterflyplot(X, title="Population Comparison")
        
        img = io.BytesIO()
        plt.savefig(img, format='png', bbox_inches='tight')
        plt.close() # Close figure to free RAM
        img.seek(0)
        
        return base64.b64encode(img.getvalue()).decode()

    except Exception as e:
        plt.figure(figsize=(6, 2))
        plt.text(0.5, 0.5, f"Error: {str(e)}", ha='center', va='center', c='red')
        plt.axis('off')
        img = io.BytesIO()
        plt.savefig(img, format='png')
        plt.close()
        img.seek(0)
        return base64.b64encode(img.getvalue()).decode()