from django.apps import AppConfig


class WagtailResumeConfig(AppConfig):
    name = "wagtail_resume"

    def ready(self):
        try:
            # pylint: disable=unused-import,import-outside-toplevel
            import wagtail_resume.signals
        except ImportError:
            pass
