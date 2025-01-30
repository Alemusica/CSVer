import pandas as pd
import os

def split_database_by_company(input_file, output_dir):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Get unique companies
    companies = df['Company'].unique()
    
    # Split data by company and save to separate files
    for company in companies:
        # Filter data for current company
        company_df = df[df['Company'] == company]
        
        # Create output filename
        safe_company_name = company.replace('/', '_').replace(' ', '_')
        output_file = f"Unified_Marine_Components_Database_{safe_company_name}.csv"
        output_path = os.path.join(output_dir, output_file)
        
        # Save to CSV
        company_df.to_csv(output_path, index=False)
        print(f"Created file for {company}: {output_file}")

if __name__ == "__main__":
    # Input file path
    input_file = "Unified_Marine_Components_Database.csv"
    
    # Output directory
    output_dir = "split_databases"
    
    # Execute split
    split_database_by_company(input_file, output_dir)
    print("Database splitting complete!")