import requests
import pandas as pd



cookie = "osano_consentmanager_uuid=3ae0fb04-a114-4f63-8308-d23fe71b60a1; osano_consentmanager=i_3APrAuV9kr0awOItVgO9ePpuGS4al5FQWkGMV5iVA5mIZc_sVJL3f5XhHsmNEtJQ6N57fiTgIJrb1OyIJEVTNdO2A6SlE71jhubvzZJ1hUDZYCRR2SSVQ3UpgPs8PqLzam4avvuGKtCMKUsyH9PPiYWp55NdZTll8gUVAALbEYhv6xvybdkZ7xLFixpzTwk1IkVbD5Fo8UXxe_Br_78SwkbbXQrkrZwbvY1rlIh1m3aXh4i_mNmLsvDSKyskbqGg_XpCz0Fh0BgzvEIVk9hu7eElvBvV63EA_U3g==; _gcl_au=1.1.618818682.1706678528; fw_se={%22value%22:%22fws2.c83318fb-352a-4de7-a44c-0d698efc26d9.1.1706678527857%22%2C%22createTime%22:%222024-01-31T05:22:07.857Z%22}; _gid=GA1.2.481348141.1706678529; _fbp=fb.1.1706678528674.109656458; _pin_unauth=dWlkPVpXTXpaakE0WXpFdE56Z3dOUzAwWkdNd0xUazJORE10WmprM1pqa3dNR0prTjJVeg; ajs_anonymous_id=ef5d5239-5588-44f8-8ded-0848575e0d6d; __stripe_mid=e7279bf1-ec24-4cf1-a9e3-734768585708b2f654; __stripe_sid=3a883f74-863a-46e2-aaad-1aa2d2b1130b946188; _uetsid=adefb640bff811ee9ea4c5de553f5bb3; _uetvid=adf09390bff811ee869685498a89c2cd; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-01-31T05:40:59.916Z%22}; _ga_EMDXDP2N4W=GS1.2.1706678528.1.1.1706679662.52.0.0; __cf_bm=l79SyhoP8zRsIn8Cc3NI_1O4gSQmxXIv44ks3I9HY1g-1706679664-1-AYiwfWw+taFSS1Xo3k8eHNd4orxG8l0f6dhHVpUNn/gEw3kwzWWdBxy6nPiJq5o6+XnmgcaJFuegqk13kh6/CRQ=; _gat_UA-000000000-1=1; _gat=1; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-01-31T05:41:55.318Z%22}; fw_uid={%22value%22:%221a6138d2-a450-4f86-ba48-44601da40ec8%22%2C%22createTime%22:%222024-01-31T05:41:55.328Z%22}; session-prd-tfm=.eJxNyU1vgjAAgOH_0rMxtGk1cHMwWYnW4EA-LoTWEoqAjgICi_99Hnd4L8_7C7Kik7oEVpHXWq5A9pBdk7ey7YHVd8NbtNRa3dusv99kCywgZ6_krlAn5dFwoZApz1y_EQp0md8tAtUjr81HatMNbXzCgnPJlhAego8yqcKeOdf6aBskdRJ8CI5TGojpGISIRV6ZzFTT9rKksVfkka9OVTizRRis8o2D7ZWpCx_8_28I5O5T02Y_cEQIj0woZrq5fnkw_X6qPNobtLpPbNkhVgnMggQX_jqe6nSsa61-BkjQ3NBxsUvkxE6yw9w9Y_Mz5uM0i-CGwQoMWnaZugKLoO0WbzB-_QEmlGjV.GJtvIw.KuYvfaeB4o_QwOptIRPALsDpxz4; _ga=GA1.1.1452898360.1706678528; _ga_2NZ40CS25B=GS1.1.1706678528.1.1.1706679715.59.0.0; _dd_s=rum=0&expire=1706680615858"


HEADERS = {
    
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    
}
    
df_skmart = pd.read_excel("skmart.xlsx", sheet_name="Sheet1") 

for i in range(0,len(df_skmart)):
    # searchinput=df_skmart.loc[i]['name']
    searchinput=input("Enter the name you want : ")
    URL= f"https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=1&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term={searchinput}&secondary_results=true&unified_search_shadow_test_enabled=false"

    responses =requests.get(URL,headers=HEADERS)
    data =responses.json()
    items = data['items']
    df_items = pd.DataFrame(items)
    df_clean = df_items[['name', 'base_price',]]
    df_clean.to_excel(f"{searchinput}.xlsx", index = False)
    

    





