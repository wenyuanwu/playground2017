test = {
  'name': 'Question 3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> select_dice(4, 24) == four_sided
          bc6c4798917b91886d7fa5f56e42878f
          # locked
          >>> select_dice(16, 64) == four_sided
          d763fd836a7bfb096222e985b161b406
          # locked
          >>> select_dice(0, 0) == four_sided
          bc6c4798917b91886d7fa5f56e42878f
          # locked
          >>> select_dice(50, 80) == four_sided
          d763fd836a7bfb096222e985b161b406
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # Make sure None isn't returned
          >>> select_dice(4, 24) == six_sided
          False
          >>> select_dice(16, 64) == six_sided
          True
          >>> select_dice(0, 0) == six_sided
          False
          >>> select_dice(50, 80) == six_sided
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}