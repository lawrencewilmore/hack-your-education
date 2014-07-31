import os, jinja2, webapp2

jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
  autoescape=True
)

class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
    self.response.out.write(*a, **kw)

  def render_str(self, template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

  def render(self, template, **kw):
    self.write(self.render_str(template, **kw))

class MainPage(Handler):
  def get(self):
    self.render('index.html')

class AboutPage(Handler):
  def get(self):
    self.render('about.html')

class ContactPage(Handler):
  def get(self):
    self.render('contact.html')

class TracksPage(Handler):
  def get(self):
    self.render('tracks.html')

class TrackPage(Handler):
  def get(self):
    self.render('track.html')

class FAQPage(Handler):
  def get(self):
    self.render('faq.html')

application = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/about/?', AboutPage),
  ('/contact/?', ContactPage),
  ('/faq/?', FAQPage),
  ('/tracks/?', TracksPage),
  ('/track/?', TrackPage)
], debug=True)
