# EasyPasswordGenerator
Easy python script with windows executable file to generate random strong passwords
<div style="text-align:center"><img style="text-align:center" src="https://img.freepik.com/premium-vector/3d-password-field-with-padlock-isolated_169241-6460.jpg" /></div>

### Password Generator
Usage: **passgen** [length] [flags]

Flags: 
- **1000** for numbers,
- **0100** for uppercase,             
- **0010** for lowercase,           
- **0001** for symbols

Example:
- passgen 8 1111  => output: **`=B@9cMLl`**           
- passgen 8 0010  => output: **`ckqmjbkg`**        
- passgen 8 1000  => output: **`75095112`**   


## Getting Started
1. Add passgen.exe file into one of the known system env path like `%SystemRoot%` or `%SystemRoot%\system32` or create one and move executable file into it.
2. Open cmd and run:
    ```
    > passgen 8
    ```
    
    result: **y!_*nqO6**

## Screenshots
<div style="text-align:center"><img style="text-align:center" src="https://raw.githubusercontent.com/MatinGhanbari/EasyPasswordGenerator/refs/heads/main/assets/images/image.png" /></div>

# Contributing
Pull requests are welcome. For changes, please open an issue first to discuss what you would like to change.
