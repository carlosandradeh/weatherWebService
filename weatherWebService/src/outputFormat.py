
class OutputFormat:

    @staticmethod
    def output_format(info_origin, info_destination):
        lines = '----------------------------------------------------------------------------------------------------------------------------------------'
        f = lines + '\nORIGIN:\n' + info_origin + '\nDESTINATION:\n' + info_destination
        return f