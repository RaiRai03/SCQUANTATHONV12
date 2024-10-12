import data_loader
import random_number_generator
import data_analyzer
import model_trainer

def main():
    # Load the data
    data = data_loader.load_data('third.csv')

    # Generate random numbers
    random_numbers = random_number_generator.generate_random_numbers(10000, 100000)

    # Combine the data and random numbers
    combined_data = pd.concat([data, random_numbers], axis=1)

    # Analyze and visualize the data
    data_analyzer.analyze_data(combined_data)

    # Train and evaluate a machine learning model
    model_trainer.train_model(combined_data)

if __name__ == '__main__':
    main()