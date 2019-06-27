from django.db import models

class User(AbsractBasedUser, PermissionsMixin):
	first_name = models.CharField(_("first name."), max_length=50)
	last_name = models.CharField(_("last name."), max_length=50)
	user_name = models.CharField(_("user name."), max_length=50)
	email = models.EmailField(_("email."), null=True, blank=True, unique=True)
	date_joined = models.DateField(_("date joined."), auto_now_add=True)
	is_promised = models.BooleanField(_("is promised."), default=False)
	

	@property
	def get_full_name(self):
		return '{0} {1}'.format(self.first_name, self.last_name)

	def __str__(self):
		return self.email


	class Meta:
		verbose_name = _("user")
		verbose_name_plural = _("users")
		ordering = ("-date_joined",)
	
	

