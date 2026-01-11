from flask import Flask, request, jsonify 
from src.accounts_registry import AccountsRegistry 
from src.personal_account import PersonalAccount 

app = Flask(__name__) 

registry = AccountsRegistry() 

@app.route("/api/accounts", methods=['POST']) 
def create_account(): 
    data = request.get_json() 
    print(f"Create account request: {data}") 
    account = PersonalAccount(data["name"], data["surname"], data["pesel"]) 
    result = registry.add_account(account) 
    if not result:
       return jsonify({"message": f"Account with pesel {data['pesel']} is already exist"}), 409
    return jsonify({"message": "Account created"}), 201 
 
@app.route("/api/accounts", methods=['GET']) 
def get_all_accounts(): 
   print("Get all accounts request received") 
   accounts = registry.get_all() 
   accounts_data = [{"name": acc.first_name, 
                     "surname": acc.last_name, 
                     "pesel": acc.national_id, 
                     "balance": acc.balance} 
                     for acc in accounts] 
   return jsonify(accounts_data), 200 
 
@app.route("/api/accounts/count", methods=['GET']) 
def get_account_count(): 
   print("Get account count request received") 
   return jsonify({"count": registry.count()}), 200 
 
@app.route("/api/accounts/<pesel>", methods=['GET']) 
def get_account_by_pesel(pesel): 
   acc = registry.get_by_national_id(pesel)
   if not acc:
      return jsonify({"message": "Account not found"}), 404
   
   return jsonify({"name": acc.first_name, 
                   "surname": acc.last_name, 
                   "pesel": acc.national_id, 
                   "balance": acc.balance}), 200 
 
@app.route("/api/accounts/<pesel>", methods=['PATCH']) 
def update_account(pesel): 
   data = request.get_json() 
   result = registry.update(pesel, data)
   if not result:
      return jsonify({"message": "Account not found"}), 404 
   return jsonify({"message": "Account updated"}), 200 
 
@app.route("/api/accounts/<pesel>", methods=['DELETE']) 
def delete_account(pesel): 
   result = registry.delete(pesel)
   if not result:
      return jsonify({"message": "Account not found"}), 404 
   return jsonify({"message": "Account deleted"}), 200

@app.route("/api/accounts/<pesel>/transfer", methods=["POST"])
def transfer(pesel):
   data = request.get_json() 
   try:
      registry.transfer(pesel, data["amount"], data["type"])
      return jsonify({"message": "Zlecenie przyjęto do realizacji"}), 200
   except Exception as e:
      message = str(e)
      response_json = jsonify({"message": message})
      match message:
         case "Account not exists":
            return response_json,404
         case "Type is invalid":
            return response_json,422
         case "Transaction error":
            return response_json,422
         case _:
            return response_json,500

