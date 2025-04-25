# Cheer Me Up App 🌞📸

**Cheer Me Up** is a simple, modern web app that lets users upload an image and get a cheerful response — like a positive message, a lighthearted joke, or a riddle. Built to showcase my cloud engineering skills using AWS services under the Free Tier.

## 🚀 Live Demo
📍[Check it out here](https://cheermeup-frontend-site.s3-website-us-east-1.amazonaws.com) — works best on desktop browsers!

---

## 🧰 Built With

- **Amazon S3** – for frontend hosting and image storage
- **Amazon API Gateway (HTTP)** – to trigger backend logic
- **AWS Lambda (Python)** – serverless compute for processing image metadata
- **AWS Cognito Identity Pool** – for secure unauthenticated access
- **AWS IAM** – custom roles and least-privilege policies
- **HTML + CSS + JavaScript** – clean and responsive frontend

---

## ✨ Features

- 📤 Upload an image and get real-time feedback
- 🔁 Each upload returns a fun response — either a joke, a riddle, or a cheerful message
- 💻 Lightweight frontend hosted on S3
- 🔐 Guest access handled securely via Cognito and IAM
- 🧠 Room for future enhancements (e.g., AWS Rekognition integration)

---

## 📂 Project Structure

```
image-analysis-app/
│
├── index.html         # Frontend code with AWS SDK
├── analyzeUploadedImage.py  # Lambda backend (in AWS)
├── README.md          # You’re here!
```

---

## 🧠 What I Learned

- How to integrate multiple AWS services in a real-world workflow
- How to handle CORS, IAM permissions, and role-based access securely
- The full deployment lifecycle of a serverless app

---

## 📸 Screenshot

![Demo Screenshot](./demo-preview.png)

---

## 👨‍💻 Author

**Seyi Aseyori**  
Aspiring Cloud Engineer | AWS Enthusiast | Lifelong Learner  
📫 [Connect on LinkedIn](https://www.linkedin.com/in/aseyiseyi/)  
🌐 [Portfolio (coming soon)](https://github.com/aseyiseyi)

---

## 📜 License

This project is open-source under the MIT License.

---

> Built with purpose and positive energy ☁️✨