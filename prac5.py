#importing data from TSV(Tab Seperated Values) textfile and storing it in database named sample.
#you should create table named csvcontents in your database with columns as shown in stri and type varchar(50)


#connecting to the database
import pymysql
connection = pymysql.connect(host="localhost", user="root", passwd="jinesh123", db="sample");
cursor = connection.cursor()

#storing the insert query inside as string in a variable
stri = """insert into csvcontents(c_br_code,c_year,c_prefix,n_srno,d_date,t_time,c_sman_code,c_dman_code,c_cust_code,c_patient,
c_doctor_code,c_doctor_name,n_total,n_st,n_cst,n_rst,n_disc_rs,n_discount,n_other_charge,n_tax_suffer,n_discount_per,
n_taxable_ret,n_non_taxable_ret,c_credit_act,n_round_off,n_counter_sale,	n_cnt_no,	n_ok,	n_cancel_flag,
d_ldate,	n_vaton,	c_order_year,	c_order_prefix,	n_order_no,	n_approved,	n_shift,	c_ipno,	c_remark,
c_patient_details,	c_card_bank_code,	c_ref_no,	c_user,	n_points,	n_point_redeem,	n_point_value,
n_pcbc_charge,	t_ltime	,d_remind_date,	n_card_reverse_dis,	c_doctor_office_code,	c_mobile,	d_ref_dt,	n_day_seq,	c_lr_no,
d_lr_date,	d_stock_sent_date,	n_cases,	n_credit_days,	n_admin_settlement,	c_terms_code,	c_reg_no,	c_email,	c_mr_code,
c_transport_code,	n_urgent,	c_modiuser,	n_tender_amt,	c_token_no,	c_coupon_code,	c_coupon_srno,c_ip_br_code,c_tran_type,
n_store_track,	c_currency_code,	n_exchange_rate,	c_computer_name,	c_sys_user,	c_sys_ip,	n_multi_payment,c_pay_code1,
n_pay_amt1,	c_pay_ac_code1,	c_pay_code2,n_pay_amt2,	c_pay_ac_code2,c_pay_code3,	n_pay_amt3,	c_pay_ac_code3,	c_pay_code4,
n_pay_amt4,	c_pay_ac_code4,c_pay_code5,n_pay_amt5,	c_pay_ac_code5,	n_marketplace_flag,	c_trader_code,n_trader_comm_total,
n_trader_charge_total,	n_trader_charge1_total,	n_inter_pur,	c_order_id,	c_debit_act_code,	c_vat_act_code,	c_purord_no,
n_share_disc,	c_integration_code,	c_cst_act_code,	c_st_act_code,	c_amt_act_code,	c_disc_act_code,	c_discrs_act_code,
c_oth_act_code,	n_update_stock,	t_from_time,	t_to_time,	c_note,	n_point_factor,	n_gst_enabled,	c_from_gst_no,
n_from_gst_type,	c_to_gst_no,	n_sale_type,	c_cgst_act_code,	n_cgst_amt,	c_sgst_act_code,	n_sgst_amt,	c_igst_act_code,
n_igst_amt,	c_cess_act_code,	n_cess_amt,	c_state_code,	c_eway_bill_no,	n_pk,	n_to_gst_type,	c_print_format_code,
c_cess_rev_act_code,	c_cgst_rev_act_code,	c_sgst_rev_act_code,	c_igst_rev_act_code,	n_service_chg,	c_port_code,
n_taxable_amt,	n_pending_points,	n_pay_ac1_flag,	n_pay_ac2_flag,	n_pay_ac3_flag,	n_pay_ac4_flag,	n_pay_ac5_flag,
d_eway_bill_date,	c_tran_gst_no,	n_dist_km,	c_service_amt_act_code,	n_ip_det_seq,	c_aadhar_no,	c_doctor_address)
 values ("""

#opening the textfile from wh
f = open("C:\\Users\\Jinesh Bagrecha\\Downloads\\B_00604118_20180912.txt", "r")
next(f)
for line in f:
    word = line.split('\t')
    c = len(word)
    query = stri
    for i in range(c):
        #if word[i] != '' and word[i] != '\t'
        query = query + "'" + word[i] + "',"
    query = query[:-1]
    query = query + ")"
    cursor.execute(query)

connection.commit()
