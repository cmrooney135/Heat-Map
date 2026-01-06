def upload_and_split_file(uploaded_file):
    if uploaded_file is not None:
        # Read lines directly from the uploaded file
        lines = uploaded_file.getvalue().decode("utf-8").splitlines()

        # Find the split point
        split_index = next(i for i, line in enumerate(lines) if "Title:, Measured Values" in line) + 1

        # Write the first part to a .txt file
        with open("temp/txt_temp.txt", "w", encoding="utf-8") as txt_file:
            txt_file.writelines(line + "\n" for line in lines[:split_index + 1])

        
        csv_lines = lines[split_index + 1:]
        header = csv_lines[0]
        data_lines = csv_lines[1:]

        # Remove the first 10 data lines
        data_lines = data_lines[12:]

        # Write the modified CSV content
        with open("temp/csv_temp.csv", "w", encoding="utf-8") as csv_file:
            csv_file.write(header + "\n")
            csv_file.writelines(line + "\n" for line in data_lines)

