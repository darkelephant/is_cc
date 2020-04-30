from flask_login import current_user
from flask_admin import AdminIndexView
from flask import redirect, flash


class HomeAdminView(AdminIndexView):
    def is_accessible(self):
        if current_user.is_authenticated:
            if current_user.login == 'admin':
                return True

    def inaccessible_callback(self, name, **kwargs):
        # return redirect(url_for(dashboard.dashboard_index))
        flash('Эта страница только для администратора')
        return redirect('/')
