# Generated by Django 3.1.7 on 2021-04-07 11:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(default='000000', max_length=13, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('branch', models.CharField(choices=[('CSE', 'Computer Science'), ('ECE', 'Electronics and Communication'), ('EEE', 'Electrical and Electronics'), ('ME', 'Mechanical'), ('BT', 'BioTech'), ('CV', 'Civil')], default='CSE', max_length=3)),
                ('credits', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('regNo', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Reg No')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phNo', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Phone No.')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='Male', max_length=7)),
                ('department', models.CharField(choices=[('CSE', 'Computer Science'), ('ECE', 'Electronics and Communication'), ('EEE', 'Electrical and Electronics'), ('ME', 'Mechanical'), ('BT', 'BioTech'), ('CV', 'Civil')], default='CSE', max_length=3)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='classroom.course')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('srn', models.CharField(max_length=13, primary_key=True, serialize=False, verbose_name='SRN')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phNo', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Phone No.')),
                ('dob', models.DateField()),
                ('age', models.PositiveIntegerField(default=18, validators=[django.core.validators.MinValueValidator(18)])),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='Male', max_length=7)),
                ('semester', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(8)])),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MinValueValidator(5.0), django.core.validators.MaxValueValidator(10.0)])),
                ('branch', models.CharField(choices=[('CSE', 'Computer Science'), ('ECE', 'Electronics and Communication'), ('EEE', 'Electrical and Electronics'), ('ME', 'Mechanical'), ('BT', 'BioTech'), ('CV', 'Civil')], default='CSE', max_length=3)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('srn',),
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.teacher')),
            ],
            options={
                'ordering': ('time',),
            },
        ),
        migrations.CreateModel(
            name='CourseEnrolled',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.course')),
                ('studentSRN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.student')),
            ],
            options={
                'verbose_name': 'Courses Enrolled',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classDate', models.DateField()),
                ('attended', models.BooleanField(default='False')),
                ('courseCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.course')),
                ('studentSRN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.student')),
            ],
            options={
                'verbose_name': 'Student Attendance',
            },
        ),
    ]
