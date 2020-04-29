from flask import app, Blueprint,render_template,request,Response,abort

submission = Blueprint(r'/submit',__name__, template_folder='templates')

@submission.route('/calculator', methods=['GET'])
def get_calculation():
    
    first_arg = request.args.get('a',None)
    second_arg = request.args.get('b',None)
    if first_arg is None or second_arg is None:
        abort(500,"valid numbers for 1st and 2nd argments are  required")

    return Response(f"result: {int(first_arg)+int(second_arg)}", content_type="plain/text")

