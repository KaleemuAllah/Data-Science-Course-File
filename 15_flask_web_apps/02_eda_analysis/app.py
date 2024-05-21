from flask import Flask, render_template, url_for
import seaborn as sns
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route('/')
def index():
    try:
        # Load the iris dataset
        iris = sns.load_dataset('iris')

        # Perform some EDA and create plots
        # Example: Pairplot of the iris dataset
        sns.pairplot(iris, hue='species')
        pairplot_path = os.path.join('static', 'pairplot.png')
        plt.savefig(pairplot_path)  # Save the plot as an image file
        plt.close()

        # Example: Boxplot of sepal_length
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='species', y='sepal_length', data=iris)
        boxplot_path = os.path.join('static', 'boxplot.png')
        plt.savefig(boxplot_path)  # Save the plot as an image file
        plt.close()

        return render_template('index.html')
    except Exception as e:
        # Log the error to the console for debugging
        app.logger.error(f"Error: {e}")
        return "An error occurred while generating the plots."

if __name__ == '__main__':
    app.run(debug=True)
