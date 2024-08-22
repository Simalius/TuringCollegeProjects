class FileConverter:
    @staticmethod
    def shopping_list_to_text(shopping_list, filename):
        with open(filename, 'w') as file:
            file.write(f"Shopping List: {shopping_list.name}\n")
            file.write("Items:\n")
            for item, details in shopping_list.items.items():
                amount = details.get('amount', 0)
                unit = details.get('unit', 'units')
                file.write(f" - {item.title()}: {amount} {unit}\n")
        return filename
