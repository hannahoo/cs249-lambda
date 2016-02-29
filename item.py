class Item(object):
    srch_id = None
    date_time = None
    site_id = None
    visitor_location_country_id = None
    visitor_hist_starrating = None
    visitor_hist_adr_usd = None
    prop_country_id = None
    prop_id = None
    prop_starrating = None
    prop_review_score = None
    prop_brand_bool = None
    prop_location_score1 = None
    prop_location_score2 = None
    prop_log_historical_price = None
    position = None
    price_usd = None
    promotion_flag = None
    srch_destination_id = None
    srch_length_of_stay = None
    srch_booking_window = None
    srch_adults_count = None
    srch_children_count = None
    srch_room_count = None
    srch_saturday_night_bool = None
    srch_query_affinity_score = None
    orig_destination_distance = None
    random_bool = None
    comp1_rate = None
    comp1_inv = None
    comp1_rate_percent_diff = None
    comp2_rate = None
    comp2_inv = None
    comp2_rate_percent_diff = None
    comp3_rate = None
    comp3_inv = None
    comp3_rate_percent_diff = None
    comp4_rate = None
    comp4_inv = None
    comp4_rate_percent_diff = None
    comp5_rate = None
    comp5_inv = None
    comp5_rate_percent_diff = None
    comp6_rate = None
    comp6_inv = None
    comp6_rate_percent_diff = None
    comp7_rate = None
    comp7_inv = None
    comp7_rate_percent_diff = None
    comp8_rate = None
    comp8_inv = None
    comp8_rate_percent_diff = None
    click_bool = None
    gross_bookings_usd = None # continuous
    booking_bool = None

    def __str__(self):
        return """== [Meta Data] ==
  Search ID: {0}
  Date: {1}
  Site: {2}
  == [Visitor] ==
  Country: {3}
  Past Star-Rating: {4}
  Past Average USD: {5}
  == [Property] ==
  Country: {6}
  ID: {7}
  Star-Rating: {8}
  Review-Score: {9}
  Branded: {10}
  Average Score1 : {11}
  Average Score2 : {12}
  Historical Price: {13}
  == [Search] ==
  srch_destination_id : {17}
  srch_length_of_stay : {18}
  srch_booking_window : {19}
  srch_adults_count : {20}
  srch_children_count : {21}
  srch_room_count : {22}
  srch_saturday_night_bool : {23}
  srch_query_affinity_score : {24}
  == [Uncategorized] ==
  Position: {14}
  Price USD: {15}
  Promotioned: {16}
  self.orig_destination_distance : {25}
  self.random_bool : {26}
  self.gross_bookings_usd : {52},
  == [User Behavior] ==
  self.click_bool : {51},
  self.booking_bool : {53}
  """.format(self.srch_id, self.date_time, self.site_id,
             self.visitor_location_country_id, self.visitor_hist_starrating, self.visitor_hist_adr_usd,
             self.prop_country_id, self.prop_id, self.prop_starrating, self.prop_review_score, self.prop_brand_bool,
             self.prop_location_score1, self.prop_location_score2, self.prop_log_historical_price,
             self.position,
             self.price_usd,
             self.promotion_flag,
             self.srch_destination_id,
             self.srch_length_of_stay,
             self.srch_booking_window,
             self.srch_adults_count,
             self.srch_children_count,
             self.srch_room_count,
             self.srch_saturday_night_bool,
             self.srch_query_affinity_score,
             self.orig_destination_distance,
             self.random_bool,
             self.comp1_rate,
             self.comp1_inv,
             self.comp1_rate_percent_diff,
             self.comp2_rate,
             self.comp2_inv,
             self.comp2_rate_percent_diff,
             self.comp3_rate,
             self.comp3_inv,
             self.comp3_rate_percent_diff,
             self.comp4_rate,
             self.comp4_inv,
             self.comp4_rate_percent_diff,
             self.comp5_rate,
             self.comp5_inv,
             self.comp5_rate_percent_diff,
             self.comp6_rate,
             self.comp6_inv,
             self.comp6_rate_percent_diff,
             self.comp7_rate,
             self.comp7_inv,
             self.comp7_rate_percent_diff,
             self.comp8_rate,
             self.comp8_inv,
             self.comp8_rate_percent_diff,
             self.click_bool,
             self.gross_bookings_usd,
             self.booking_bool
             )

    def __getitem__(self, name):
        if name=="srch_id": return self.srch_id
        elif name=="date_time": return self.date_time
        elif name=="price_usd": return self.price_usd
        elif name=="site_id": return self.site_id
        elif name=="visitor_hist_starrating": return self.visitor_hist_starrating
        elif name=="visitor_hist_adr_usd": return self.visitor_hist_adr_usd
        elif name=="prop_country_id": return self.prop_country_id
        elif name=="prop_id": return self.prop_id
        elif name=="prop_starrating": return self.prop_starrating
        elif name=="prop_review_score": return self.prop_review_score
        elif name=="prop_brand_bool": return self.prop_brand_bool
        elif name=="prop_location_score1": return self.prop_location_score1
        elif name=="prop_location_score2": return self.prop_location_score2
        elif name=="prop_log_historical_price": return self.prop_log_historical_price
        else: raise Exception("Unhandled name " + name)

    def load_from_fields(self, fields):
        self.srch_id = fields[0]
        self.date_time = fields[1]
        self.site_id = fields[2]
        self.visitor_location_country_id = fields[3]
        self.visitor_hist_starrating = None if fields[4] == "NULL" else fields[4]
        self.visitor_hist_adr_usd = None if fields[5] == "NULL" else fields[5]
        self.prop_country_id = fields[6]
        self.prop_id = fields[7]
        self.prop_starrating = fields[8]
        self.prop_review_score = None if fields[9] == "NULL" else fields[9]
        self.prop_brand_bool = fields[10]
        self.prop_location_score1 = None if fields[11] == "NULL" else fields[11]
        self.prop_location_score2 = None if fields[12] == "NULL" else fields[12]
        self.prop_log_historical_price = fields[13]
        self.position = fields[14]
        self.price_usd = fields[15]
        self.promotion_flag = fields[16]
        self.srch_destination_id = fields[17]
        self.srch_length_of_stay = fields[18]
        self.srch_booking_window = fields[19]
        self.srch_adults_count = fields[20]
        self.srch_children_count = fields[21]
        self.srch_room_count = fields[22]
        self.srch_saturday_night_bool = fields[23]
        self.srch_query_affinity_score = fields[24]
        self.orig_destination_distance = fields[25]
        self.random_bool = fields[26]
        self.comp1_rate = fields[27]
        self.comp1_inv = fields[28]
        self.comp1_rate_percent_diff = fields[29]
        self.comp2_rate = fields[30]
        self.comp2_inv = fields[31]
        self.comp2_rate_percent_diff = fields[32]
        self.comp3_rate = fields[33]
        self.comp3_inv = fields[34]
        self.comp3_rate_percent_diff = fields[35]
        self.comp4_rate = fields[36]
        self.comp4_inv = fields[37]
        self.comp4_rate_percent_diff = fields[38]
        self.comp5_rate = fields[39]
        self.comp5_inv = fields[40]
        self.comp5_rate_percent_diff = fields[41]
        self.comp6_rate = fields[42]
        self.comp6_inv = fields[43]
        self.comp6_rate_percent_diff = fields[44]
        self.comp7_rate = fields[45]
        self.comp7_inv = fields[46]
        self.comp7_rate_percent_diff = fields[47]
        self.comp8_rate = fields[48]
        self.comp8_inv = fields[49]
        self.comp8_rate_percent_diff = fields[50]
        self.click_bool = fields[51]
        self.gross_bookings_usd = fields[52]
        self.booking_bool = fields[53]
