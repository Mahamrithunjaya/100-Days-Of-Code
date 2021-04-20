import smtplib

my_email = "*********@gmail.com"
password = "******"

for _ in range(20):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="******@yahoo.com",
            msg="Subject:Hello\n\nThis is the body of my email."
        )

    print(f"Done {_}")
