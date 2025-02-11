# Pseudocode for orders.ipynb Exercise

class Order:

    def __init__(self):
        # Initialise by loading the necessary datasets from the Olist data module
        # (For example: self.orders, self.order_items, self.order_reviews, self.order_payments, self.geolocation, etc.)
        pass

    def get_wait_time(self):
        """
        Returns a DataFrame with the following columns:
         - order_id
         - wait_time: days between purchase and delivery (as a decimal)
         - expected_wait_time: days between purchase and estimated delivery (as a decimal)
         - delay_vs_expected: delay in days if actual delivery is later than estimated (0 if early)
         - order_status
        """
        # 1. Load the orders dataframe (already available as self.orders)
        # 2. Filter the orders: keep only those with a delivered status
        #    e.g., delivered_orders = orders[orders['order_status'] == 'delivered']
        #
        # 3. Convert the date columns (order_purchase_timestamp, order_delivered_customer_date,
        #    estimated_delivery_date) from strings to datetime objects using pd.to_datetime()
        #
        # 4. Calculate 'wait_time' as:
        #    (order_delivered_customer_date - order_purchase_timestamp) expressed in days as a decimal.
        #    Use subtraction of datetime objects and then convert the result to a float representing days.
        #
        # 5. Calculate 'expected_wait_time' as:
        #    (estimated_delivery_date - order_purchase_timestamp) in decimal days.
        #
        # 6. Calculate 'delay_vs_expected' as:
        #    If order_delivered_customer_date is later than estimated_delivery_date,
        #    compute the difference (in days) else set the value to 0.
        #
        # 7. Construct a new DataFrame containing:
        #    order_id, wait_time, expected_wait_time, delay_vs_expected, order_status
        #
        # 8. Return the resulting DataFrame.
        pass

    def get_review_score(self):
        """
        Returns a DataFrame with:
         - order_id
         - dim_is_five_star: 1 if review_score is 5, else 0
         - dim_is_one_star: 1 if review_score is 1, else 0
         - review_score
        """
        # 1. Load the order_reviews dataframe (e.g., self.order_reviews)
        #
        # 2. For each row, determine the review_score.
        #
        # 3. Create a new column 'dim_is_five_star':
        #    Use a mapping (or apply a lambda) to set the value to 1 when review_score == 5, else 0.
        #
        # 4. Similarly, create 'dim_is_one_star':
        #    Set the value to 1 when review_score == 1, else 0.
        #
        # 5. Construct and return a new DataFrame with the columns:
        #    order_id, dim_is_five_star, dim_is_one_star, review_score.
        pass

    def get_number_items(self):
        """
        Returns a DataFrame with:
         - order_id
         - number_of_items: total number of items per order
        """
        # 1. Load the order_items dataframe (e.g., self.order_items)
        #
        # 2. Group the data by 'order_id' and count the number of items (each row represents an item).
        #    Use groupby and count (or size) to determine the count per order.
        #
        # 3. Rename the resulting count column to 'number_of_items'.
        #
        # 4. Return the new DataFrame with the two columns.
        pass

    def get_number_sellers(self):
        """
        Returns a DataFrame with:
         - order_id
         - number_of_sellers: number of unique sellers involved in the order
        """
        # 1. Load the order_items dataframe (e.g., self.order_items)
        #
        # 2. Group the dataframe by 'order_id' and calculate the number of unique sellers using .nunique() on the seller_id column.
        #
        # 3. Rename the resulting column to 'number_of_sellers'.
        #
        # 4. Return the DataFrame with order_id and number_of_sellers.
        pass

    def get_price_and_freight(self):
        """
        Returns a DataFrame with:
         - order_id
         - price: total price paid by the customer for the order
         - freight_value: total freight value paid by the customer for the order
        """
        # 1. Load the order_payments dataframe (e.g., self.order_payments)
        #
        # 2. Group by 'order_id' and aggregate the 'price' and 'freight_value' columns.
        #    You can use .agg() with sum as the aggregation function, if orders may have multiple payments.
        #
        # 3. Return the resulting DataFrame with columns: order_id, price, freight_value.
        pass

    def get_training_data(self, with_distance_seller_customer=False):
        """
        Returns the complete training DataFrame, merging all the features created by the previous methods.
        The final DataFrame must not contain any NaN values.

        Optionally, if with_distance_seller_customer is True, also merge the seller-customer distance.
        """
        # 1. Call each of the previous methods to get their corresponding DataFrames:
        #    - wait_time_df = self.get_wait_time()
        #    - review_score_df = self.get_review_score()
        #    - number_items_df = self.get_number_items()
        #    - number_sellers_df = self.get_number_sellers()
        #    - price_freight_df = self.get_price_and_freight()
        #
        # 2. Merge these DataFrames on 'order_id'.
        #    Start by merging two DataFrames at a time (e.g., using pd.merge()).
        #
        # 3. If with_distance_seller_customer is True:
        #    - Get the distance DataFrame using self.get_distance_seller_customer()
        #    - Merge it into the final DataFrame.
        #
        # 4. Remove any rows that contain NaN values (using .dropna()).
        #
        # 5. Return the final training DataFrame.
        pass

    def get_distance_seller_customer(self):
        """
        (Optional) Returns a DataFrame with:
         - order_id
         - distance_seller_customer: the average distance in km between the customer and the seller(s)
        """
        # 1. Load the required datasets:
        #    - Orders data (for customer location)
        #    - Order_items (to link orders to sellers)
        #    - Sellers and geolocation data (for seller location)
        #
        # 2. For each order, retrieve the customer's geolocation.
        #
        # 3. For each seller involved in the order, retrieve the seller's geolocation.
        #
        # 4. Use the provided haversine_distance function (from olist.utils) to compute the distance between the customer's and seller's coordinates.
        #
        # 5. If an order involves multiple sellers, compute the average distance across all sellers.
        #
        # 6. Return a DataFrame with order_id and distance_seller_customer.
        pass
