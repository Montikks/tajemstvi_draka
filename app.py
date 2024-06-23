from app import app

if __name__ == '__main__':
    import os
    print(f"Static folder: {os.path.abspath(app.static_folder)}")  # Přidáno pro ladění
    print(f"Template folder: {os.path.abspath(app.template_folder)}")  # Přidáno pro ladění
    app.run(debug=True)
