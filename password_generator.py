import string
import secrets
import argparse

# --- 1. تعریف کاراکترها / Define Character Sets ---
# کاراکترهای قابل استفاده در رمز عبور
# Available characters for password generation
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SPECIAL = string.punctuation # شامل کاراکترهای خاص مانند !@#$%^&*

def generate_secure_password(length, use_numbers, use_special):
    """
    Generates a cryptographically secure random password.
    یک رمز عبور امن با امنیت رمزنگاری بالا تولید می‌کند.

    :param length: The desired length of the password. (طول رمز عبور)
    :param use_numbers: Boolean to include digits. (شامل اعداد باشد یا نه)
    :param use_special: Boolean to include special characters. (شامل کاراکترهای خاص باشد یا نه)
    :return: Generated password as a string. (رمز عبور تولید شده)
    """
    characters = UPPERCASE + LOWERCASE

    if use_numbers:
        characters += DIGITS
    if use_special:
        characters += SPECIAL
        
    # بررسی حداقل کاراکترهای انتخاب شده
    # Safety check to ensure the character pool is not empty
    if not characters:
        raise ValueError("Cannot generate password with no character sets selected.")
    
    # استفاده از secrets.choice (امن) به جای random.choice (ناامن)
    # Use secrets.choice (secure) instead of random.choice (insecure)
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def main():
    """
    Handles command-line arguments and runs the password generator.
    مدیریت آرگومان‌های خط فرمان و اجرای ژنراتور رمز عبور.
    """
    # تنظیمات Argparse برای دریافت ورودی‌ها از خط فرمان
    # Setup Argparse to receive inputs from the command line
    parser = argparse.ArgumentParser(
        description="A Python script to generate cryptographically secure passwords."
    )
    
    # آرگومان طول رمز (اختیاری) - اگر وارد نشود 12 کاراکتر در نظر گرفته می‌شود
    # Optional length argument (default is 12)
    parser.add_argument(
        '-l', '--length', 
        type=int, 
        default=12, 
        help='Length of the password (default: 12)'
    )
    
    # فلگ عدم استفاده از اعداد (اختیاری)
    # Optional flag to exclude numbers
    parser.add_argument(
        '--no-numbers', 
        action='store_false', 
        dest='numbers', 
        help='Exclude numbers from the password'
    )

    # فلگ عدم استفاده از کاراکترهای خاص (اختیاری)
    # Optional flag to exclude special characters
    parser.add_argument(
        '--no-special', 
        action='store_false', 
        dest='special', 
        help='Exclude special characters from the password'
    )

    args = parser.parse_args()

    try:
        if args.length < 8:
             # توصیه امنیتی: طول رمز نباید کمتر از 8 باشد
             # Security recommendation: Password length should be at least 8
            print("Warning: Password length should be at least 8 for good security.")

        password = generate_secure_password(
            args.length, 
            args.numbers, 
            args.special
        )
        
        # نمایش رمز عبور تولید شده
        # Print the generated password
        print("\n🔑 Generated Secure Password:")
        print(f"   {password}")
        print("-" * 30)
        print("Note: This password was generated using Python's cryptographically secure 'secrets' module.")
        
    except ValueError as e:
        print(f"Error: {e}")
        parser.print_help() # نمایش راهنمای استفاده در صورت بروز خطا

# نقطه ورود استاندارد برنامه
# Standard Python entry point
if __name__ == "__main__":
    main()
