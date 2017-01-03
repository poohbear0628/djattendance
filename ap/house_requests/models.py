from django.db import models

class RequestInterface:
  def get_category(self):
    return self.get_type_display()
  def get_status(self):
    return self.get_status_display()
  def get_date_created(self):
    return self.date_requested
  def get_trainee_requester(self):
    return self.trainee_author

  @staticmethod
  def get_create_url():
    raise NotImplementedError
  def get_absolute_url(self):
    raise NotImplementedError
  @staticmethod
  def get_detail_template():
    raise NotImplementedError
  @staticmethod
  def get_button_template(isTA):
    raise NotImplementedError
