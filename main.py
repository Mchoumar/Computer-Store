from fpdf import FPDF
import pandas as px
from sndemail import Email

df = px.read_csv("articles.csv", dtype={"id": str})


class Article:
    def __init__(self, articleId):
        self.articleId = articleId
        self.name = df.loc[df["id"] == self.articleId, "name"].squeeze()
        self.price = df.loc[df["id"] == self.articleId, "price"].squeeze()

    def stock(self):
        """When someone buys an item it subtracts from the stock"""
        df.loc[df["id"] == self.articleId, "in stock"] -= 1
        df.to_csv("articles.csv", index=False)

    def available(self):
        """Checks if the article is available"""
        availability = df.loc[df["id"] == self.articleId, "in stock"].squeeze()
        if availability > 0:
            return availability
        else:
            return False


class Receipt:
    def __init__(self, article):
        self.article = article

    def invoice(self):
        """
        This script creates pdf file.
        """
        # Initiate creation of pdf
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        # Makes a cell for the text
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=30, h=10, txt=f"Receipt nr.{self.article.articleId}", ln=1)
        pdf.cell(w=30, h=10, txt=f"Article: {self.article.name}", ln=1)
        pdf.cell(w=30, h=10, txt=f"Price: {self.article.price}", ln=1)

        # Outputs the data into the pdf file
        pdf.output("invoice.pdf")


print(df)

article_id = input("Enter the id of the article: ")
article_object = Article(article_id)
mail = Email()

if article_object.available():
    receipt = Receipt(article_object)
    article_object.stock()
    mail.send()
else:
    print("Article doesn't exist!")
