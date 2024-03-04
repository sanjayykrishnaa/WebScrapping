import requests 
import pandas as pd

competitor_list = [
    {
        'url' : "https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term=apple&secondary_results=true&unified_search_shadow_test_enabled=false",
        'cookie' :"osano_consentmanager_uuid=3ae0fb04-a114-4f63-8308-d23fe71b60a1; osano_consentmanager=i_3APrAuV9kr0awOItVgO9ePpuGS4al5FQWkGMV5iVA5mIZc_sVJL3f5XhHsmNEtJQ6N57fiTgIJrb1OyIJEVTNdO2A6SlE71jhubvzZJ1hUDZYCRR2SSVQ3UpgPs8PqLzam4avvuGKtCMKUsyH9PPiYWp55NdZTll8gUVAALbEYhv6xvybdkZ7xLFixpzTwk1IkVbD5Fo8UXxe_Br_78SwkbbXQrkrZwbvY1rlIh1m3aXh4i_mNmLsvDSKyskbqGg_XpCz0Fh0BgzvEIVk9hu7eElvBvV63EA_U3g==; _gcl_au=1.1.618818682.1706678528; _fbp=fb.1.1706678528674.109656458; _pin_unauth=dWlkPVpXTXpaakE0WXpFdE56Z3dOUzAwWkdNd0xUazJORE10WmprM1pqa3dNR0prTjJVeg; ajs_anonymous_id=ef5d5239-5588-44f8-8ded-0848575e0d6d; __stripe_mid=e7279bf1-ec24-4cf1-a9e3-734768585708b2f654; _gid=GA1.2.1691903149.1707113975; _uetsid=8812bb50c3ee11ee82226f32f2417d34; _uetvid=adf09390bff811ee869685498a89c2cd; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-02-05T06:59:08.227Z%22}; _ga_EMDXDP2N4W=GS1.2.1707116347.3.0.1707116348.59.0.0; __cf_bm=LwQV__LCtAocjzzgBAejF5EuZuSmkhugdZS2QPTUlAI-1707126815-1-AavrUEbOhn6tMdO8u921Hy9tS83y+HsDFEKZVLd4QcDBdhmG/zyOvf+E/kog94TEVAb8T6tU6q6GRiMsWSIw0oU=; fw_se={%22value%22:%22fws2.ee5fcf27-5d18-4cbc-bd66-d79e9ecf3c51.4.1707126817329%22%2C%22createTime%22:%222024-02-05T09:53:37.329Z%22}; __stripe_sid=b701f479-ee10-47b5-9939-cd054e7bf3d12af86f; _gat_UA-000000000-1=1; _gat=1; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-02-05T10:05:41.728Z%22}; fw_uid={%22value%22:%221a6138d2-a450-4f86-ba48-44601da40ec8%22%2C%22createTime%22:%222024-02-05T10:05:41.739Z%22}; session-prd-tfm=.eJxNyU1vgjAAgOH_0rMxQIof3JwItIH6MZXRC6G1hHYUDYUhmP33edzhvTzvC-RlK0wFvLKojZiB_CFaXTSi6YDXtf1bjDBG3pu8u3-LBnhAjLhiIZd7idFlQjaReD1_o82d6_hu4k79w-r1g27RAukM7kM0UX9nxWlQZWnSEX8zUGlBMhEdnwOV6JPKNHom4UlnIzKouU70C5dFepR7dRnJxC2ijla8xRUN7Qf7_7Vrs3AwSAc9c1yXpWubj2hxi7BNPwdZpIGF1P1Jpo1DFIfknMHyOPcp6wnmUYHS-gB9WigVBYcdVTxPPpa3TaxX0XDq6FOtwAz0RrS5vAHPdZZLuIDw9w85Kmid.GKJEdQ.0csX9fCy2U0M5M2SMpm823b3wUA; _ga=GA1.1.1452898360.1706678528; _dd_s=rum=0&expire=1707128442149; _ga_2NZ40CS25B=GS1.1.1707126815.4.1.1707127542.42.0.0"
            },
    
    {
        'url' : "https://shop.wegmans.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frecency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term",
        'cookie' : "AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; _fbp=fb.1.1707114173560.22496243; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiY0MjI2NDc0OTk2MDQ5NDQ5MDY5MTEwNTQwOTc4MDU4MzczMTM2MlIRCNqpvL_XMRgBKgRJTkQxMAPwAdqpvL_XMQ==; _pin_unauth=dWlkPVpXTXpaakE0WXpFdE56Z3dOUzAwWkdNd0xUazJORE10WmprM1pqa3dNR0prTjJVeg; _gcl_au=1.1.960365967.1707114176; wfm.tracking.sessionStart=1707114175752; wfmStoreId=16; at_check=true; inRedirectGoldPanAudience=1; ajs_anonymous_id=5e34fc02-ed1b-4520-8137-b3ec2ed46f96; wfm.tracking.s10=1; wfm.tracking.x2p=1; sa-user-id=s%253A0-dd1cc11d-8698-5d62-43b1-2f3fc6cbfa5e.2jygkpVFtbsNb9ZSVCx51kjTz66HTEBhVEqPO%252FmmkBk; sa-user-id-v2=s%253A3RzBHYaYXWJDsS8_xsv6XjEvxIg.%252B3J6hqjVfloBvITPtRB%252FomJhhR7kMzHwXpqaY6JQQFs; sa-user-id-v3=s%253AAQAKIOoj-Lx98xVsUmyfoMHWCoGY8vKxNRQ1wavzsJ4RdJrOEAEYAyDPz92tBjABOgSE7j3kQgQaouKi.LTTnTDkmlSS21leJdUf%252FJ%252F0kGOMkK2hmQ8xTboVGtZA; _pin_unauth=dWlkPVpXTXpaakE0WXpFdE56Z3dOUzAwWkdNd0xUazJORE10WmprM1pqa3dNR0prTjJVeg; at_check=true; ajs_anonymous_id=5e34fc02-ed1b-4520-8137-b3ec2ed46f96; __stripe_mid=4fd8e580-daca-4cbd-ae5e-4f8cdf0cec87bd0cd3; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; __cf_bm=C7_gNo.F1kWDQ9xM0DPnc3nbkU2pd9BFOq4PuOBNREY-1707126346-1-AR5KWy6Q8jv4+E7PrW48aIINFYhxcR1dXelvSFNWxzPOdv5F6nnGMnPIhdBSI0vK/xTf7DdoTP2NZh2yVuuIxBs=; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19759%7CMCMID%7C42264749960494490691105409780583731362%7CMCAAMLH-1707731147%7C12%7CMCAAMB-1707731147%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1707133547s%7CNONE%7CMCSYNCSOP%7C411-19766%7CMCCIDH%7C0%7CvVersion%7C5.5.0; dotcomSearchId=b6a36f93-4787-41c7-938d-fe831be54ba7; lux_uid=170712636450567982; __stripe_sid=fc5f2a4b-0e0d-4a86-9f5e-d021a764450c35a8d0; s_gpv=Search%20Results:%20apple%20|%20Wegmans; _uetsid=fff9f4e0c3ee11ee850347c44c25bf4f; _uetvid=fffa0540c3ee11ee805c0f0c5910c41d; session-prd-weg=.eJwdjs2OgjAYAN-lZzUUUAPHVWRL_CAoCvRCEGoo1mooyM9m333JHuYyl5kflN0bpipk33Oh2AJlb9Y8c8lki-y26WajmFL8JbP29WAS2YiNXnVzCx5wj1wmgn3uWatZ4kK_jjNToYvPTVhvuiMbUlMBLuB0cvRjdBkgSlt_75hwxhWNSnGMQpPWMAQRYOpSkXKiiLxONPHueRzyoA4x7FPDn2AMzj1P41Obx-v_VqKLB6nfXRkP6ribp55Wx2L8KRPggTyNZXxR5Cmqcv6AqOj9yRnmtuEn2qrGfCt1ooz860D7xPTGEJLc4RD4y6Wr9eBZp4P4PmsbghaoU6zJeIlsc61ttltDt37_AA7-aJ8.GKJAzQ.qY2EC6LNo7h3UtR-Klf-tRTqxII; _dd_s=rum=0&expire=1707127505767; mbox=session#3aa16538cfc4423aad776ad835c1a349#1707128467|PC#3aa16538cfc4423aad776ad835c1a349.41_0#1770371362"},
    
    {
        'url' : "https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=60&offset=0&search_is_autocomplete=true&search_provider=ic&search_term=",
        'cookie' : "_gcl_au=1.1.1050395268.1707115544; _gid=GA1.2.281675837.1707115545; _fbp=fb.1.1707115545429.2098486304; _pin_unauth=dWlkPVpXTXpaakE0WXpFdE56Z3dOUzAwWkdNd0xUazJORE10WmprM1pqa3dNR0prTjJVeg; __cf_bm=CmLs3w9zyRsZ0yvt1sZyPJrpLTEzjLrMQ1gTIj9k5K8-1707115545-1-Af4YxaeZN6uSireXDDMwmNlOSbRwF/+OST0EbJprRAdCC09Y8e4aAK9uUwnTtmeRS45UW54gOzwqfCB5V3Otn/A=; BVBRANDID=523ba0c3-20fc-40c9-afda-6b7888f405d9; BVBRANDSID=75dd7649-eabe-4baa-a8be-deb92dbb6e51; loyaltyID=undefined; ajs_anonymous_id=fe520955-bf26-44ee-9838-81fd0e516101; _pin_unauth=dWlkPVpXTXpaakE0WXpFdE56Z3dOUzAwWkdNd0xUazJORE10WmprM1pqa3dNR0prTjJVeg; ajs_anonymous_id=fe520955-bf26-44ee-9838-81fd0e516101; __stripe_mid=54d1b214-59ce-4fdb-a1dc-ff805b3e0925642da6; __stripe_sid=05b45c21-f28a-4df7-80aa-c1acf2e429031ec15a; _ga=GA1.2.834404714.1707115545; _gat_UA-47434162-1=1; session-sprouts=.eJwdjstygjAAAP8lZ8fBQLVwU2xtGALVRgJeGAyhhJcOATTp9N_L9LCXvez-gLTouSyBU2SN5AuQ3nnfZh3vBuAM_TgbyaUUty4dbjXvgAO48srrgYlQeOis0SoQnr2c5YrBSM1oBpvp2tj3i4vWqNrqRL_XF8K0T44GPqAh2J-qRBkWptjySVmGBKtEMzOhkcAKSdRF-hJ7RUaPIqyQEe5nyFZj8RAJPQ0ZfflvxbCpUXUfc_qUvjtPtfbI6WrKYyzC7qRyepaobcp8_sCEPQL99gzI2QhMYykKotZugia8q6Pr1vr63EHurisxHL43MkSu-oDPasNiegMLMErepyIHDrReoWUbJvz9A5VDaiU.GKIV7A.gdEmcqebbMDD_uS1cPc-92hNOWo; _uetsid=3080eaa0c3f211eeabcb4b0ca1cfaeea; _uetvid=30812fb0c3f211ee9e849124622cd037; _ga_LPZ816BHL5=GS1.1.1707115544.1.1.1707115628.58.0.0; _dd_s=rum=0&expire=1707116528579"
    }
]

searchterm = 'Apple'
cookie = competitor_list[2]['cookie']

HEADERS = {   
    
    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    'Cookie': cookie    
}

URL = competitor_list[2]['url'] + 'apple'
responses = requests.get(URL, headers=HEADERS)
data = responses.json()
items = data.get('items')

for item in items:
    print(item['name'])

print("-------------FILTERED DATA----------------")

for item in items:
    for category in item.get('categories'):
        # print(category.get('name'))
        if(category.get('name')=='Fresh Fruits'):
        # if(category.get('name')=='Fruits'):
            if(searchterm in item.get('name')):
                print(item.get('name'))
                
        # print(category.get('name'))
        # if (searchterm in item.get('name')):
        #     print(item.get('name'))