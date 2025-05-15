import pandas as pd

# Load datasets
interactions = pd.read_csv("C:\\Users\\kianr\\Desktop\\UNI\\BSUmarketplace\\BSU_Interation.csv")
users = pd.read_csv("C:\\Users\\kianr\\Desktop\\UNI\\BSUmarketplace\\BSU_User.csv")
products = pd.read_csv("C:\\Users\\kianr\\Desktop\\UNI\\BSUmarketplace\\BSU_Product.csv")

# Print column names to inspect
print("User columns:", users.columns.tolist())
print("Interaction columns:", interactions.columns.tolist())


df = pd.merge(interactions, users[['userId', 'course']], on='userId')

# Strip whitespace from column headers
users.columns = users.columns.str.strip()
interactions.columns = interactions.columns.str.strip()
products.columns = products.columns.str.strip()

# Re-run your merge after cleaning
df = pd.merge(interactions, users[['userId', 'course']], on='userId')



def recommend_products(user_id: str, course: str, top_n: int = 10):
    is_new_user = user_id not in df['userId'].unique()

    # Step 1: Define course + 'All' products
    eligible_products = products[
    (products['course'].str.lower() == course.lower()) | 
    (products['course'].str.lower() == 'all')
]


    # Step 2: Filter ratings for eligible products
    eligible_product_ids = eligible_products['productId'].unique()
    filtered_df = df[df['productId'].isin(eligible_product_ids)]

    # Step 3: Course-based ratings (excluding current user)
    course_ratings = filtered_df[(filtered_df['course'] == course) & (df['userId'] != user_id)]
    course_avg = course_ratings.groupby('productId')['rating'].mean().reset_index()
    course_avg['source'] = 'course'

    # Step 4: Category/global-based ratings
    global_avg = filtered_df.groupby('productId')['rating'].mean().reset_index()
    global_avg['source'] = 'overall'

    # Step 5: Remove products the user has already rated (if existing)
    if not is_new_user:
        user_rated = df[df['userId'] == user_id]['productId'].tolist()
        course_avg = course_avg[~course_avg['productId'].isin(user_rated)]
        global_avg = global_avg[~global_avg['productId'].isin(user_rated)]

    # Step 6: Combine and prioritize
    combined = pd.concat([course_avg, global_avg])
    combined = combined.drop_duplicates(subset='productId', keep='first')
    combined = combined.sort_values(by='rating', ascending=False).head(top_n)

    # Add product names
    combined = pd.merge(combined, products[['productId', 'productName']], on='productId', how='left')

    return combined[['productName', 'rating', 'source']]

# Example usage
if __name__ == '__main__':
    user_id = input("Enter user ID (e.g., US3): ")
    course = input("Enter course (STEM, Arts, Humanities, Business, Sports): ")

    recommendations = recommend_products(user_id, course)
    if recommendations.empty:
        print("\nNo recommendations found.")
    else:
        print("\nTop Recommended Products:")
        print(recommendations.to_string(index=False))
