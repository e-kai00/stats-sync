from flask import flash, redirect, url_for, render_template


def handle_bad_request(e):
    print(f'error happened {str(e)}')
    return render_template('error/400.html'), 400

def page_not_found(e):
    print(f'error happened {str(e)}')
    return render_template('error/404.html'), 404

def internal_server_error(e):
    print(f'error happened {str(e)}')
    return render_template('error/500.html'), 500

def handle_sqlalchemy_error(e, redirect_to='spend_snap'):
    flash('Check if all fields are filled correctly and try again.', 'error')
    print(f'database error happened {str(e)}')
    return redirect(url_for(redirect_to))
