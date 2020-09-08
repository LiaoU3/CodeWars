# https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python

def format_duration(seconds):
    secs = seconds % 60
    mins = (seconds//60)%60
    hours = ((seconds//60)//60)%24
    days = (((seconds//60)//60)//24)%365
    years = (((seconds//60)//60)//24)//365
    time =[years, days, hours, mins, secs]
    if seconds == 0:
        return 'now'
    return ('{}{}{}{}{}{}{}{}{}'.format(     '%d year%s%s ' %(years, 's' if years > 1 else '', '' if (days == 0 and hours == 0 and mins == 0 and secs == 0) or (years != 0 and time.count(0) == 3 ) else ',') if years > 0 else '',
                                            'and ' if days != 0 and years != 0 and hours == 0 and mins == 0 and secs == 0 else '',                                    
                                            '%d day%s%s ' %(days, 's' if days > 1 else '',  '' if (hours == 0 and mins == 0 and secs == 0) or (hours != 0 and mins == 0 and secs == 0) or (hours == 0 and mins != 0 and secs == 0) or(hours == 0 and mins == 0 and secs != 0) else ',')if days > 0 else '',
                                            'and ' if hours != 0 and(years != 0 or days != 0) and mins == 0 and secs == 0 else '',                                    
                                            '%d hour%s%s ' %(hours, 's' if hours > 1 else '','' if(mins == 0 and secs == 0) or (mins == 0 and secs != 0) or (mins != 0 and secs == 0) else ',')if hours > 0 else '',
                                            'and ' if mins != 0 and(years != 0 or days != 0 or hours != 0) and secs == 0 else '',                                    
                                            '%d minute%s%s ' %(mins, 's' if mins > 1 else '','' if (secs == 0) or (mins != 0 and secs!=0) else ',')if mins > 0 else '',
                                            'and ' if secs != 0 and(years != 0 or days != 0 or hours != 0 or mins != 0) else '',
                                            '%d second%s' %(secs, 's' if secs > 1 else '')if secs >0 else '' )).strip()

# times = [("year", 365 * 24 * 60 * 60), 
#          ("day", 24 * 60 * 60),
#          ("hour", 60 * 60),
#          ("minute", 60),
#          ("second", 1)]

# def format_duration(seconds):

#     if not seconds:
#         return "now"

#     chunks = []
#     for name, secs in times:
#         qty = seconds // secs
#         if qty:
#             if qty > 1:
#                 name += "s"
#             chunks.append(str(qty) + " " + name)

#         seconds = seconds % secs

#     return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

                                            

print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))