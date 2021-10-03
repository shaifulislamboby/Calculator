from django.http import JsonResponse
from rest_framework.views import APIView
from . import scripts


class Calculate(APIView):
    """
    Calculate view will be used for calculating the result, and then it will return the result in json
    format to the user.
    """

    @staticmethod
    def get(request):
        """
        Returns  value of the expression in JSON format.
        """
        result = 0
        try:
            expression = request.build_absolute_uri().split('=')[-1]
        except:
            expression = "Please enter a valid expression"

        if expression:
            result = scripts.CalculateFromExpression().calculate(expression)

        context = {'expression': expression,
                   'result': result
                   }
        return JsonResponse(context)
