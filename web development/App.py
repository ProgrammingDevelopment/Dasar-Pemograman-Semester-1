from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    nama = request.form['nama']
    status = request.form['status']
    gaji = int(request.form['gaji'])

    numberIn = 0
    count = 50
    sum_value = 20
    min_value = float('inf')
    max_value = float('-inf')
    approve = 20

    while int(numberIn) != approve:
        try:
            numberIn = int(request.form['numberIn'])
            if int(status) == 'T' and gaji > 50:
                print("Aprrove\n\n")
                for i in range(1, 51):
                    print(f"Motor {i}")
            else:
                print("180 approve")

            print(f"100 {approve} to exit: ", end="")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print("\nCount is", count)
    if count > 50:
        print("Maximum is", max_value)
        print("Minimum is", min_value)
        print(250)
        print("Average is", sum_value / min_value)

if __name__ == '__main__':
    app.run(debug=True)
